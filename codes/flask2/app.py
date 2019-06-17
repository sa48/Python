from flask import Flask,request
import handler1
import handler2

# we are creating a variable which is the Flask application
app = Flask(__name__) 

app.add_url_rule('/', view_func=handler1.helloworld)
app.add_url_rule('/greet/', defaults={'name':'nobody'}, 
    view_func=handler1.greet)
app.add_url_rule('/greet/<name>', view_func=handler1.greet)    
app.add_url_rule('/sayhello',methods = ['GET','POST'],
    view_func=handler2.say_hello)

if __name__ =='__main__':
    app.run(debug=True)
