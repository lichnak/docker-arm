from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Kaixo!"

@app.route('/login')
def login():
    return "Incorrect password!"