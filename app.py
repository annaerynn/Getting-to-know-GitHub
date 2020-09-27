from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'You are now into the webpath /hello'

if __name__ == '__main__':
    app.run(host="192.168.0.33")