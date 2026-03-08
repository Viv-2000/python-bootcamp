# importing necessary library
from flask import Flask

###WSGI Application
app = Flask(__name__)

@app.route('/')
def homepage():
    return "hello there"


if __name__=="__main__":
    app.run(debug=True)

'''
app = Flask(__name__)
    
    - It creates an instance of the Flask class
    - which will be your WSGI (Web Server Gateway Interface) application.

@app.route('/')
def homepage():
    return "hello" 
    
    - this decorator, is used to call the function defined under it
    - the route '/' is specifically for the home directory
    - any return statements will print the return of the function on the root directory of your webpage. 

if __name__=="__main__":
    app.run(debug=True)
    
    - this is the main part of your code file
    - when we put app.run(debug=True), the debug=True parameter ensures that saving of file reruns our app 
    -  this is helpful in development stage 

'''