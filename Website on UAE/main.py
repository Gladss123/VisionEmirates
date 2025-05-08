# main.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/heritage')
def heritage():
    return render_template('heritage.html')

@app.route('/golden')
def golden():
    return render_template('golden.html')

@app.route('/space')
def space():
    return render_template('space.html')

@app.route('/achieve')
def achieve():
    return render_template('achieve.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

if __name__ == '__main__':
    app.run(debug=True)


