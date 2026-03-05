from flask import Flask, render_template

###WSGI Application
app = Flask(__name__)

@app.route('/')
def homepage():
    return "hello there mate. this is the root directory of your webapp"


## - the route '/index' is specifically for the index directory after root 
@app.route('/subdirectory')
def sub_directory():
    return "congrats, you made it to the first sub directory"


##  render_template redirects to an html or css document
## the html docmument must be present in templates folder in the same directory as the code
@app.route('/redirection')
def redirect():
    return render_template('redirection.html')



## making sub-sub-directory and redicting to an html page
@app.route('/redirection/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)

