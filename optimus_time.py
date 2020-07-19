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

def split(input_w):
    #return [Work(w_in.name, w_in.dur/w_in.due, w_in.due), Work(w_in.name, w_in.dur/w_in.due, w_in.due)]
    L = []
    for n in range(0,input_w.due):
        #for p in range(0,l):
        L.append(Work(input_w.name,round(input_w.dur/input_w.due,1),input_w.due-n))
            #if input_work[p].due-n <= 0:
                
    return L

def schedule(input_w_l):
    S = []
    for W in input_w_l:
        S.append(split(W))
    final = []
    max_due = input_w_l[-1].due
    for d in range(max_due):
        A = []
        for subject in S:
            try:
                A.append(subject[d])
            except:
                True
        final.append(A)
    return final

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
    un_proc_tasks = [Work(session[n][0],int(session[n][1]),int(session[n][2])) for n in session]
    if len(un_proc_tasks) > 0:
        un_proc_tasks.sort(key=lambda x: x.due, reverse=False)
        sched = schedule(un_proc_tasks)
        return render_template('calendar.html',sched=sched)
    return render_template('calendar.html')

with app.test_request_context():
    print(url_for('index'))