import os
import time
import threading
import webbrowser
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000/")

t = threading.Thread(target=open_browser)
t.start()
app.run() #进入等待状态，按CTRL和C终止运行