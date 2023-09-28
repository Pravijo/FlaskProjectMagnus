from flask import Flask
sample = Flask(__name__)


@sample.route("/Welcome")
def welcome():
    return 'Welcome to Webpage using Flask'


@sample.route("/add")
def add():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = a+b
    return f"The sum of {a} and {b} is {c}"


"""
@sample.route("/add")
def add():
    return "Enter two numbers in the URL like this: /add?num1=5&num2=3"


@sample.route("/add/<int:num1>/<int:num2>")
def add_numbers(num1, num2):
    c = num1 + num2
    return f"The sum of {num1} and {num2} is {c}."
"""


if __name__ == '__main__':
    sample.run(debug=True)
