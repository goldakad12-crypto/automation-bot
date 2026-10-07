import os
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


# إعداد قاعدة البيانات وتحديث الجدول لدعم عدة عملاء/متاجر (عبر page_id)
def init_db():
  conn = sqlite3.connect('automation_store.db')
  cursor = conn.cursor()
  cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_id TEXT NOT NULL,
            keyword TEXT NOT NULL,
            reply TEXT NOT NULL,
            UNIQUE(page_id, keyword)
        )
    ''')
  conn.commit()
  conn.close()


init_db()


@app.route('/')
def home():
  return '🚀 سحابة الأتمتة المحلية تعمل بكفاءة تامة وجاهزة لخدمة العملاء!'


# إضافة أو تحديث قاعدة رد خاصة بمتجر معين (page_id)
@app.route('/add_rule', methods=['POST'])
def add_rule():
  data = request.json
  page_id = data.get('page_id')
  keyword = data.get('keyword')
  reply = data.get('reply')

  if not page_id or not keyword or not reply:
    return jsonify(
        {'error': 'الرجاء إدخال معرف الصفحة (page_id) والكلمة والرد'}
    ), 400

  try:
    conn = sqlite3.connect('automation_store.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT OR REPLACE INTO rules (page_id, keyword, reply) VALUES (?, ?,'
        ' ?)',
        (page_id, keyword, reply),
    )
    conn.commit()
    conn.close()
    return jsonify({
        'message': (
            f'تمت إضافة القاعدة للمتجر ({page_id}) للكلمة ({keyword}) بنجاح!'
        )
    }), 200
  except Exception as e:
    return jsonify({'error': str(e)}), 500


# فحص التعليق وإعطاء الرد الخاص بصفحة المتجر المطلوب
@app.route('/simulate_comment', methods=['POST'])
def simulate_comment():
  data = request.json
  page_id = data.get('page_id')
  comment_text = data.get('comment', '').strip()

  if not page_id or not comment_text:
    return jsonify(
        {'error': 'الرجاء تحديد معرف الصفحة (page_id) ونص التعليق'}
    ), 400

  conn = sqlite3.connect('automation_store.db')
  cursor = conn.cursor()
  cursor.execute(
      'SELECT keyword, reply FROM rules WHERE page_id = ?', (page_id,)
  )
  rules = cursor.fetchall()
  conn.close()

  matched_reply = None
  for keyword, reply in rules:
    if keyword in comment_text:
      matched_reply = reply
      break

  if matched_reply:
    return jsonify({
        'status': 'success',
        'matched': True,
        'reply_sent': matched_reply,
        'message': f'تم جلب الرد بنجاح لمتجر ({page_id})!',
    }), 200
  else:
    return jsonify({
        'status': 'ignored',
        'matched': False,
        'message': 'التعليق لا يحتوي على كلمة مفتاحية مسجلة لهذا المتجر.',
    }), 200


if __name__ == '__main__':
  # الاستماع على المنفذ المخصص للسحابة أو 5000 محلياً
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
