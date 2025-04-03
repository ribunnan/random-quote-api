from flask import Flask, jsonify
import random
import os
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # ✅ 关键设置，防止 Unicode 转义

# 从 words.json 文件读取词汇库
with open("words.json", encoding="utf-8") as f:
    words = json.load(f)

@app.route('/')
def home():
    return "欢迎使用日语 N1 词汇 API。访问 /api/random-word 获取一个随机的日语单词。"

@app.route('/api/random-word')
def random_word():
    word = random.choice(words)
    return jsonify(word)  # 结构化 JSON 返回，字段名 + 正常文字

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
