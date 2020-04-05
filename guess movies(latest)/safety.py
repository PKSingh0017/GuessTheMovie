from flask import *
import random                                 #letter used=-1, wrong letter =-2, wrong movie=-5

movies_hollywood = ['intersteller', 'jurassic world', 'the matrix',
'forrest gump', 'the dark knight', 'the godfather', 'gravity',
'the avengers', 'the fast and the furious','the lord of the rings',
'star wars', 'shutter island','the incredibles', 'mad max fury road',
'annabelle comes home', 'inception', 'divergent', 'justice league',
'gladiator', 'fight club', 'deadpool', 'the hangover', 'suicide squad',
'mission impossible', 'skyfall']

movies = movies_hollywood[ : ]
A = 20
B = 20
C = 20
R = 1
ag = []
bg = []
cg = []
ae = False
be = False
ce = False
display = False

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[];
    for i in range(n):
        if ref[i]==letter:
            temp.append(letter)
        else:
            temp.append(qn_list[i])
    qn_new="".join(str(x) for x in temp)
    return qn_new

qn = random.choice(movies)
movies.remove(qn)
nqn = create_question(qn)
refer = "lets play"
app = Flask(__name__)

@app.route('/')
@app.route('/',methods=['POST'])
def getValueA():
    global nqn, qn, refer, A, B, C, n2, ae, be, ce, R, display, result, ag, bg, cg
    if ae:
        return render_template('index.html',p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -A")

    if request.method=='POST':
        refer = 'lets play'
        n2=request.form['name']                    #entered letter is being stored in n2

        if n2==qn:
            display = qn
            ag.append(qn)
            refer = "Well Done GROUP -A"
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            if not be:
                return render_template('b.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -B")
            else:
                return render_template('c.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -C")
        elif len(n2) == 1:
            if is_present(n2, qn):
                nqn = unlock(nqn, qn, n2)
                A -= 1
            else:
                refer = 'incorrect'
                A -= 2
        elif len(n2)>1:
            refer = "incorrect movie"
            A -= 5

        if A <= 0:
            ae = True
            A = "ELEMINATED"
            ag.append(qn+'*')
            display = qn
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            refer = "GROUP -A WAS ELEMINATED"
            if not be:
                if ce:
                    result = "******Group B Wins******"
                    return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)
                return render_template('b.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -B")
            else:
                result = "******Group C Wins******"
                return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)

    return render_template('index.html',p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -A")


@app.route('/b.html')
@app.route('/b.html',methods=['POST'])
def getValueB():
    global nqn, qn, refer, A, B, C, n2, ae, be, ce, R, display, result, ag, bg, cg
    if be:
        return render_template('b.html',p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -B")

    if request.method=='POST':
        refer = 'lets play'
        n2=request.form['name']                    #entered letter is being stored in n2

        if n2==qn:
            display = qn
            bg.append(qn)
            refer = "Well Done GROUP -B"
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            if not ce:
                return render_template('c.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -C")
            else:
                return render_template('index.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -A")
        elif len(n2) == 1:
            if is_present(n2, qn):
                nqn = unlock(nqn, qn, n2)
                B -= 1
            else:
                refer = 'incorrect'
                B -= 2
        elif len(n2)>1:
            refer = "incorrect movie"
            B -= 5

        if B <= 0:
            be = True
            B = "ELEMINATED"
            bg.append(qn+'*')
            display = qn
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            refer = "GROUP -B WAS ELEMINATED"
            if not ce:
                if ae:
                    result = "******Group C Wins******"
                    return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)
                return render_template('c.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -C")
            else:
                result = "******Group A Wins******"
                return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)

    return render_template('b.html',p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -B")

@app.route('/c.html')
@app.route('/c.html',methods=['POST'])
def getValueC():
    global nqn, qn, refer, A, B, C, n2, ae, be, ce, R, display, result, ag, bg, cg
    if ce:
        return render_template('c.html', p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -C")

    if request.method=='POST':
        refer = 'lets play'
        n2=request.form['name']                    #entered letter is being stored in n2

        if n2==qn:
            display = qn
            cg.append(qn)
            refer = "Well Done GROUP -C"
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            if not ae:
                return render_template('index.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -A")
            else:
                return render_template('b.html',p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -B")
        elif len(n2) == 1:
            if is_present(n2, qn):
                nqn = unlock(nqn, qn, n2)
                C -= 1
            else:
                refer = 'incorrect'
                C -= 2
        elif len(n2)>1:
            refer = "incorrect movie"
            C -= 5

        if C <= 0:
            ce = True
            C = "ELEMINATED"
            cg.append(qn+'*')
            display = qn
            qn = random.choice(movies)
            movies.remove(qn)
            nqn = create_question(qn)
            refer = "GROUP -C WAS ELEMINATED"
            if not ae:
                if be:
                    result = "******Group A Wins******"
                    return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)
                return render_template('index.html', p=nqn, q = refer, display = display, rA = A, rB = B, rC = C, title = "GROUP -A")
            else:
                result = "******Group B Wins******"
                return render_template('result.html',res = result, ag=ag, bg=bg, cg=cg)

    return render_template('c.html',p=nqn, q = refer, rA = A, rB = B, rC = C, title = "GROUP -C")

if __name__=='__main__':
    app.run(host = 'localhost', port = 8080)
