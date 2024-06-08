#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    output = f""
    for i in range (num):
        output += f"{i}\n"
    print(output)
    return output
        

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        output = str(num1 + num2)
        print(output)
        return output
    elif operation == "-":
        output = str(num1 - num2)
        print(output)
        return output
    elif operation == "*":
        output = str (num1 * num2)
        print(output)
        return output
    elif operation == "div":
        output = str (num1 / num2)
        print(output)
        return output
    elif operation == "%":
        output = str (num1 % num2)
        print(output)
        return output
    else:
        print("Unkown operator found")
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

