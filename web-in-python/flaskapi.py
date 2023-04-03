from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'Salam': 'Donya'}

if (__name__ == '__main__'):
    app.run(port=5556, debug=True)