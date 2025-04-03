from flask import Flask
import random
import os

app = Flask(__name__)

# 语录库
quotes = [
    "生活就像骑自行车，要想保持平衡就得继续前行。",
    "不要轻言放弃，否则对不起自己。",
    "当你足够努力，幸运自然会跟上来。",
    "星光不问赶路人，时光不负有心人。",
    "保持热爱，奔赴山海。"
]

@app.route('/')
def home():
    return "欢迎使用语录 API。访问 /api/random-quote 获取一句话。"

@app.route('/api/random-quote')
def random_quote():
    return random.choice(quotes)  # 直接返回纯文本，不是 JSON

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
