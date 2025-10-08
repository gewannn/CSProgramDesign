from flask import Flask, render_template, request
from openai import OpenAI
import time
import threading
import webbrowser
import os

API_KEY = "sk-28361ced6b5f4da891c15d91a466579b"
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com/v1")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)
@app.route('/', methods=['GET',"POST"])
def index():
    result = None
    prompt = None
    if request.method == 'POST':
        prompt = request.form.get('prompt','').strip()
        if prompt:
            try:
                response = client.chat.completions.create(
                    model="deepseek-reasoner",
                    messages=[{'role':'user', 'content':prompt}],
                    stream=False,
                    max_tokens=1024,
                    temperature=0.7
                    )
                result = response.choices[0].message.content
            except Exception as e:
                result = f"API 调用错误: {str(e)}"
    return render_template('index.html', result=result, prompt=prompt)
    
def open_browser():
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    t = threading.Thread(target=open_browser)
    t.start()
    app.run(debug=True, host='127.0.0.1', port=5000)
            