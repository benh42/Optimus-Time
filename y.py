class Work():
    def __init__(self,name,dur,due):
        self.name = name 
        self.dur = dur
        self.due = due
    def __repr__(self):
        return f"{self.name}: {self.dur}: {self.due}"

input_work = [Work("math",1,3),Work("chem",2,4),Work("english",5,7)]
input_work.sort(key=lambda x: x.due, reverse=False)

def split(input_w):
    #return [Work(w_in.name, w_in.dur/w_in.due, w_in.due), Work(w_in.name, w_in.dur/w_in.due, w_in.due)]
    L = []
    for n in range(0,input_w.due):
        #for p in range(0,l):
        L.append(Work(input_w.name,input_w.dur/input_w.due,input_w.due-n))
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

#list of tasks should be assigned to calendar slots