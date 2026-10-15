from flask import Flask, render_template_string

app = Flask(__name__)

# قائمة المنتجات في المتجر (تضم المنتج القديم والمنتج الجديد)
PRODUCTS = [
    {
        "title": "حزمة WPS Office الذكية (نسخة رسمية مجانية + بريميوم)",
        "category": "أدوات مكتبية وتعديل مستندات",
        "description": (
            "أفضل بديل مجاني وسريع لإدارة وتعديل ملفات Word و Excel و PDF بدقة"
            " عالية، مع أدوات ذكاء اصطناعي متقدمة."
        ),
        "price": "مجاني / متوفر بريميوم",
        "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe",
        "link": "https://yynbx.com/g/nv5qc75bd92c966d96710e10b6b7ca/",
    },
    {
        "title": "GuinRank 7 - منصة الذكاء الاصطناعي والسيو الشاملة",
        "category": "تسويق إلكتروني وتحسين محركات البحث",
        "description": (
            "احصل فوراً على 500 رصيد مجاني + 10 مقالات لتصدر نتائج البحث في جوجل"
            " وصناعة سكربتات ريلز بالذكاء الاصطناعي، مع كود خصم 5% (GUINPRO5) عند"
            " الترقية."
        ),
        "price": "مجاني (هدية 500 رصيد) / خصم 5%",
        "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe",  # يمكنك استبدال الرابط بصورة GuinRank الخاصة بك
        "link": "https://www.guinrank.com/?ref=REF-1727-1CBC",
    },
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجرك الرقمي والتقني الذكي</title>
    <meta name="mitgo-verification" content="4e121221-dc7c-4c1a-9cc1-de4ba4f1aca7" />
    <style>
        :root {
            --bg-main: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --success: #4ade80;
            --btn-bg: #2563eb;
            --btn-hover: #1d4ed8;
        }
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            margin: 0;
            padding: 0;
        }
        header {
            text-align: center;
            padding: 50px 20px;
            border-bottom: 1px solid #334155;
        }
        header h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
        }
        header p {
            color: var(--text-muted);
            margin: 0;
        }
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
        }
        .card {
            background-color: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0,0,0,0.4);
        }
        .card img {
            width: 100%;
            height: 160px;
            object-fit: cover;
        }
        .card-content {
            padding: 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .category {
            font-size: 12px;
            color: var(--accent);
            text-transform: uppercase;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .card h3 {
            margin: 0 0 10px 0;
            font-size: 18px;
            color: var(--text-main);
        }
        .card p {
            color: var(--text-muted);
            font-size: 14px;
            line-height: 1.5;
            margin: 0 0 15px 0;
            flex-grow: 1;
        }
        .price-row {
            display: flex;
            
