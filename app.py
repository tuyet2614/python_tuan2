from logging import debug
from flask import Flask
from flask import render_template, request
import pandas as pd
app = Flask(__name__)

df = pd.read_csv('advanced_python.csv', sep=';')

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

@app.route('/thread/<string:posttitle>')
def getpage(posttitle):
    return f"querying post via {posttitle}"

@app.route('/student/<string:MSV>')
def Student(MSV):
    student = df[df['student code'] == MSV]
    return student.to_html()

@app.route('/student/class/<string:className>')
def StudentCode(className):
    student2 = df[df['First name'] == className]
    return student2.to_html()

@app.route('/student/code', methods=['POST', 'GET'])
def getStudentviacode():
    if request.method == 'POST':
        studentcode = request.form.get('studentcode')
        result = df[df['student code'] == studentcode].to_html()
        return result
    return render_template('studentfilter.html')

if __name__ == '__main__':
    app.run()
    
