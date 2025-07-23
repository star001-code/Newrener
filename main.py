
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/chats')
def chats():
    return render_template('chats.html')

# لتشغيل السيرفر محليًا
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
