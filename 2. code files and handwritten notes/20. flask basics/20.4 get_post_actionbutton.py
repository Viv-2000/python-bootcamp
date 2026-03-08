from flask import Flask, render_template, request

app = Flask(__name__)



# the form is in the root directory itself


# by default, methods=['GET'] which is when we are tryin to get info, 'POST' is when we are subitting info
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        name = request.form['name']
        return f'hello {name}'
    return render_template('form.html')



# since here methods is only = ['POST'], this /submit directory is unaccessible directly 
# user must POST some data through a form, where action='/submit', and cannot GET this url on his own
# since only 1 method in @app.ruote(), by default request.method == ['POST'] is True


@app.route('/submit', methods=['POST'])
def submit():
  
    name = request.form['name']
    return f'hello there {name}'


if __name__=="__main__":
    app.run(debug=True)