from flask import request

def helloworld():
    return '<h1>Hello world!</h1>'

def greet(name):
    return 'Good morning, ' + name

def add(x,y):
    return 'Total is ' + str(x+y)

