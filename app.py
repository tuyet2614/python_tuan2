from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/author')
def author():
    #return 'Hi'
    return render_template('author.html')

@app.route('/add')
def add():
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    return f"{a} + {b} = {a+b}"


@app.route('/mul/<int:a>/<int:b>')
def mul(a,b):
    return f"{a} * {b} = {a*b}"

if __name__ == '__main__':
    app.run()
    
