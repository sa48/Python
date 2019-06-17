from flask import request

def say_hello():
    name = request.args.get('name') or request.form.get('name')
    return "Hello." + (name or '')