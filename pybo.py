from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!' # Hello Pybo! 를 출력
