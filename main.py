from flask import Flask, render_template, request
from helpers import addition, subtraction, multiplication, division

app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = addition(var_1, var_2)
    elif(operation == 'Subtraction'):
        result = subtraction(var_1, var_2)
    elif(operation == 'Multiplication'):
        result = multiplication(var_1, var_2)
    elif(operation == 'Division'):
        result = division(var_1, var_2)
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('sum.html', entry=entry)


