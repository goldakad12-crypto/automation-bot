from flask import Flask, render_template_string

app = Flask(__name__)

# قائمة المنتجات والروابط الترويجية (قم بتحديث الرابط لاحقاً بروابط Admitad الخاصة بك)
PRODUCTS = [
    {
        "id": 1,
        "title": "منظومة طاقة شمسية منزلية متكاملة",
        "category": "طاقة متجددة",
        "description": "أحدث ألواح ومنظومات الإنفرتر لتوليد طاقة نظيفة ومستدامة على مدار الساعة.",
        "price": "تبدأ من $499",
        "image": "https://images.unsplash.com/photo-1509391365330-f7096e210137?auto=format&fit=crop&w=600&q=80",
        "link": "https://your-admitad-affiliate-link-1.com"
    },
    {
        "id": 2,
        "title": "بطارية ليثيوم حديثة لتخزين الطاقة",
        "category": "بطاريات وملحقات",
        "description": "بطارية ذات كفاءة عالية وعمر افتراضي طويل، مثالية لأنظمة الطاقة الشمسية الحديثة.",
        "price": "$299",
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=600&q=80",
        "link": "https://your-admitad-affiliate-link-2.com"
    },
    {
        "id": 3,
        "title": "دليل البرمجة وأتمتة المهام بلغة بايثون",
        "category": "منتجات رقمية",
        "description": "كتاب رقمي شامل ومبسط لاحتراف بايثون وتطوير سكربتات الأتمتة المربحة.",
        "price": "$19",
        "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80",
        "link": "https://your-admitad-affiliate-link-3.com"
    },
    {
        "id": 4,
        "title": "قوالب تسويقية احترافية لوسائل التواصل",
        "category": "محتوى وتسويق",
        "description": "حزمة تصاميم جاهزة تزيد من تفاعل العملاء وتدعم حملات التسويق الرقمي.",
        "price": "$29",
        "image": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=600&q=80",
        "link": "https://your-admitad-affiliate-link-4.com"
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجرك الرقمي والتقني الذكي</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent: #38bdf8;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --btn-bg: #2563eb;
            --btn-hover: #1d4ed8;
            --success: #4ade80;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            direction: rtl;
        }
        header {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border-bottom: 1px solid #334155;
            padding: 35px 20px;
            text-align: center;
        }
        header h1 {
            color: var(--accent);
            margin: 0 0 10px 0;
            font-size: 28px;
        }
        header p {
            color: var(--text-muted);
            margin: 0;
            font-size: 16px;
        }
        .container {
            max-width: 1100px;
            margin: 40px auto;
            padding: 0 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
        }
        .card {
            background: var(--card-bg);
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
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .price {
            color: var(--success);
            font-weight: bold;
            font-size: 16px;
        }
        .btn {
            background-color: var(--btn-bg);
            color: white;
            text-align: center;
            padding: 10px 15px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.2s;
        }
        .btn:hover {
            background-color: var(--btn-hover);
        }
        footer {
            text-align: center;
            padding: 30px;
            color: #64748b;
            font-size: 14px;
            border-top: 1px solid #334155;
            margin-top: 60px;
        }
    </style>
</head>
<body>

    <header>
        <h1>متجرك الرقمي والتقني الذكي</h1>
        <p>اكتشف أفضل المنتجات والحلول التقنية الموصى بها مع روابط مباشرة</p>
        <meta name="mitgo-verification" content="4e121221-dc7c-4c1a-9cc1-de4ba4f1aca7" />
    </header>

    <div class="container">
        <div class="grid">
            {% for p in products %}
            <div class="card">
                <img src="{{ p.image }}" alt="{{ p.title }}">
                <div class="card-content">
                    <span class="category">{{ p.category }}</span>
                    <h3>{{ p.title }}</h3>
                    <p>{{ p.description }}</p>
                    <div class="price-row">
                        <span class="price">{{ p.price }}</span>
                    </div>
                    <a href="{{ p.link }}" target="_blank" class="btn">معاينة أو طلب المنتج</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <footer>
        جميع الحقوق محفوظة &copy; 2026 - منصة الويب السحابية الآمنة
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, products=PRODUCTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
