from flask import Flask, url_for, render_template, request, make_response, session, jsonify
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


@app.route('/work-info')
def index():
    return jsonify([session[n] for n in session])

@app.route('/optimus-time', methods=['POST', 'GET'])
def login():
    session['test'] = Work('Test',1,2)

    if request.method == 'POST':
        name = request.form['name']
        dur = request.form['duration_hr']
        due = request.form['due_in_x']
        session[f"{name}"] = [name,dur,due]

    session.pop('test')

    return render_template('optimus_time.html')

@app.route('/calendar', methods=['GET','POST'])
def calendar():
    if request.method == 'POST':
        if request.form['clear'] == "1":
            session.clear()
    un_proc_tasks = [Work(x[0],x[1],x[2]) for x in session]
    sched = schedule(un_proc_tasks)
    return render_template('calendar.html',sched=sched)

with app.test_request_context():
    print(url_for('index'))