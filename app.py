from flask import Flask
import random
import os
import json

app = Flask(__name__)

# 从 words.json 文件读取词汇库
with open("words.json", encoding="utf-8") as f:
    words = json.load(f)

@app.route('/')
def home():
    return "欢迎使用日语 N1 词汇 API。访问 /api/random-word 获取一个随机的日语单词。"

@app.route('/api/random-word')
def random_word():
    word = random.choice(words)
    return f"{word['word']}（{word['kana']}）：{word['meaning']}（{word['pos']}，重音：{word['pron']}）"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
