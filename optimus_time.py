from flask import Flask, url_for, render_template, request
from markupsafe import escape
app = Flask(__name__) 

def valid_login(username,password):
    return False
def log_the_user_in(username):
    return render_template('hello.html',name=username)

@app.route('/')
def index():
    return 'index'

@app.route('/optimus-time', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        dur = request.form['duration_hr']
        due = request.form['due_in_x']
        
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('optimus_time.html', error=error)


    list_of_assignments = request.form['assingments']
    #"do algorithm on list"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))