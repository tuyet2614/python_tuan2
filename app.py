from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/author')
def author():
    #return 'Hi'
    return render_template('author.html')

if __name__ == '__main__':
    app.run()
    