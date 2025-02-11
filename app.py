
from flask import Flask
from flask import render_template 

app = Flask(__name__)

@app.route('/')
def home():
    message = "Hello, World"
    return render_template('welcome.html', message=message) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)