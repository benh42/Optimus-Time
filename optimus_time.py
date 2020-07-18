from flask import Flask, url_for, render_template, request, make_response,session,jsonify
from markupsafe import escape
app = Flask(__name__) 
app.secret_key = b'O*D:&fO#O&OPS;{Q:l'

class Work():
    def __init__(self,name,dur,due):
        self.name = name
        self.dur = dur
        self.due = due
    def __repr__(self):
        return f"{self.name} : {self.dur} : {self.due}"

def valid_login(username,password):
    return False
def log_the_user_in(username):
    return render_template('hello.html',name=username)

@app.route('/work-info')
def index():
    return jsonify([session[n] for n in session])

@app.route('/optimus-time', methods=['POST', 'GET'])
def login():
    session["test"] = [1,2]

    if request.method == 'POST':
        name = request.form['name']
        dur = request.form['duration_hr']
        due = request.form['due_in_x']
        session[f"{name}"] = [dur,due]


    return render_template('optimus_time.html')

with app.test_request_context():
    print(url_for('index'))