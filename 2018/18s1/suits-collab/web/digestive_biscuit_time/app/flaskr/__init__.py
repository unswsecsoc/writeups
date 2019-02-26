from flask import Flask, render_template, request, g, session, redirect, abort
import sqlite3
import time
import base64
import datetime

app = Flask(__name__)
app.secret_key = 'lolplsbsecure'

def makeSession(username):
    session = username+","+str(int(time.time()))
    return base64.b64encode(session.encode("utf-8")).decode("utf-8")

def getName(session):
    if session == "None":
        return None
    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT USERNAME FROM USERS WHERE SESSION = ?",(session,));
    user = c.fetchone()
    if not user:
        return None
    name = user[0]
    conn.close()
    return name

def getData():
    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM POSTS");
    return c.fetchall()
    return False
    return [("admin","Just logged in! The sunset in sydney today is beautiful.","6/4/18 2018")]

def userExists(username):
    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM USERS WHERE USERNAME = ?",(username,));
    if c.fetchone():
        return True
    conn.close()
    return False

def createUser(username, password):
    conn = sqlite3.connect('/db.sqlite3')
    session = makeSession(username)
    c = conn.cursor()
    c.execute("INSERT INTO USERS VALUES (?,?,?)",(username,password,session))
    conn.commit()
    conn.close()
    return session

def loginUser(username, password):
    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    if userExists(username):
        c.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = ?",(username,))
        attempt = c.fetchone()[0]
        if  attempt != password:
            return None
    else:
        return None
    session = makeSession(username)
    c.execute("UPDATE USERS SET SESSION = ? WHERE USERNAME = ?",(session,username))
    conn.commit()
    conn.close()
    return session

def makePost(username,content):
    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    timeNow = datetime.datetime.now().strftime("%d/%m/%y")
    c.execute("INSERT INTO POSTS VALUES(?,?,?)",(username,content,timeNow))
    conn.commit()
    conn.close()

def sessionUpdate(session):
    redirect_to_index = redirect('/')
    response = app.make_response(redirect_to_index)
    response.set_cookie('session',session)
    return response

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        if "session" not in request.cookies:
            abort(502)
        if "post" not in request.form:
            abort(502)
        makePost(getName(request.cookies["session"]),request.form["post"])
        return redirect("/")
    if "session" in request.cookies:
        n = getName(request.cookies["session"])
        if not n:
            return redirect("/login")
        flag=None
        if n == "admin":
            flag="FLAG{sUns3ts_r_b002fu11}"
        return render_template("index.html", name=n, data=getData(),flag=flag)
    else:
        return redirect("/login")

@app.route('/logout',methods=['GET'])
def logmeout():
    if "session" not in request.cookies:
        abort(502)
    session = request.cookies["session"]
    redirect_to_index = redirect('/login')
    response = app.make_response(redirect_to_index)
    response.set_cookie('session',value='',expires=0)
    if getName(request.cookies["session"]) == "admin":
        return response

    conn = sqlite3.connect('/db.sqlite3')
    c = conn.cursor()
    c.execute("UPDATE USERS SET SESSION = ? WHERE SESSION = ?",("None",session))
    conn.commit()
    conn.close()
    return response

@app.route('/login', methods=['GET','POST'])
def new():
    if request.method == "POST":
        if "username" not in request.form:
            abort(502)
        if "password" not in request.form:
            abort(502)
        if "action" not in request.form:
            abort(502)

        username = request.form["username"]
        password = request.form["password"]
        action = request.form["action"]

        if len(username) <= 0 or len(password) <= 0:
            return render_template("new.html",err="Empty username/password")

        if action == "create":
            if userExists(username):
                return render_template("new.html",err="User exists")
            else:
                session = createUser(username,password)
                return sessionUpdate(session)

        elif action == "login":
            session = loginUser(username,password)
            if not session:
                return render_template("new.html",err="Incorrect username/password")
            return sessionUpdate(session)
        else:
            abort(502)

    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)
