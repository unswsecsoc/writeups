#!/usr/bin/python3
# Code by Zachery Ellis (Top Hat) 30 March 2018 

import sqlite3, hashlib, random
from flask import Flask, render_template, session, url_for, request, redirect
from flask_mail import Mail, Message
import os

import init_db

database = "test.db"
web_port = '1099'
flag = 'FLAG{Safebook_might_be_a_misnomer}'
domain = "gmail.com"
sender_email = os.getenv("SENDER_EMAIL", "hashban.recovery@unswsecurity.com")
sender_password = os.getenv("SENDER_PASSWORD", "hunter2")
MAX_ZUCC_MEMES = 28

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = sender_email,
    MAIL_PASSWORD = sender_password,
    SECRET_KEY = 'kVvbUy8nyDujl3e3lyMaOiHw0O1Pwpf2Ex7m4YNHYA9gWa1ha2EeBE9dve-kjoG7t9I'
)

mail = Mail(app)


@app.before_first_request
def setup():
    init_db.main()


def write_password(user, password):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    print ("Stored new password",password)
    c.execute('''UPDATE users SET password = ? WHERE username = ?''', (password, user))
    conn.commit()
    conn.close()


def get_pass(username):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT password from users WHERE username = ?", (username,))
    try:
        password = c.fetchone()[0]
    except:
        password = c.fetchone()
    print ("Ret val password:'"+str(password)+"'")
    conn.close()
    return password

def get_email(username):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT email from users WHERE username = ?", (username,))
    try:
        email = c.fetchone()[0]
    except:
        email = None
    print ("Ret val email:'"+str(email)+"'")
    conn.close()
    return email

def email_reset(reset_link, destination_email):
    msg = mail.send_message(
        'Password Reset',
        sender=sender_email,
        recipients=[destination_email],
        body=("Please use the following link to reset your account: " + reset_link)
    )


def create_user(username, name, email, password):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO users(username, name, email, password) VALUES(?,?,?,?)''',
                (username, name, email, password))
    connection.commit()
    connection.close()

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
        username = request.form.get('username', '').strip()
        if username == "":
            return render_template('register.html', message="Username cannot be empty")

        name = request.form.get('name', '').strip()
        if name == "":
            return render_template('register.html', message="Name cannot be empty")
        
        email = request.form.get('email', '').strip()
        if email == "":
            return render_template('register.html', message="Email cannot be empty")

        password = request.form.get('password', '').strip()
        if password == "":
            return render_template('register.html', message="Password cannot be empty")

        if (get_pass(username) != None):
            return render_template('register.html', message="Username already registered")

        safe_pass = hashlib.md5(password.encode("utf")).hexdigest()
        create_user(username, name, email, safe_pass)

        return render_template('register.html', message="Registered user: "+username+"")
    
    else:
        return render_template('register.html')


@app.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username', '')
        recovery = hashlib.md5(username.encode("utf")).hexdigest()
        recovery_addr = request.url_root+"recover/"+username+"/"+recovery
        print (recovery_addr)
        if get_email(username) != None:
            email_reset(recovery_addr, get_email(username))
            return render_template('forgot_password.html', message="Email Sent!")
        else:
            return render_template('forgot_password.html', message="User not found")
    else:   
        return render_template('forgot_password.html', message="")

    
@app.route('/home', methods=['GET','POST'])
def display_user():
    if 'username' in session:
        username = session['username']
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT name from users WHERE username=?", (username,))
        try:
            Name = c.fetchone()[0]
        except:
            Name = c.fetchone()
        conn.close()
        val_details = {}
        if (Name != None):
            val_details = {"Name":Name}
        image = "meme-"+str(random.randrange(1,MAX_ZUCC_MEMES))+".jpg"
        return render_template('user_page.html', user_details=val_details, img_file=image)
    else:
        return redirect(url_for('login'))


@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('display_user'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        response = "Attempting login with "+str(username)+":"+str(password)
        safe_pass = hashlib.md5(password.encode("utf")).hexdigest()
        user_pass = get_pass(username)
        if user_pass != None:
            if user_pass == safe_pass:
                print("Logged in as",username)
                session['username'] = username
                session.logged_in = True
                session.modified = True 
                return redirect(url_for('display_user'))    
            else:
                print("Login unsuccessful")
        return render_template('login.html', message = "Invalid username/password, maybe try the reset password option?") 
    return render_template('login.html')   


@app.route('/recover/<username>/<hash_str>', methods=['GET','POST'])
def recover(username, hash_str):
    if request.method == 'GET':
        if get_pass(username) != None:
            if hash_str == hashlib.md5(username.encode("utf")).hexdigest():
                message = "Verification passed, please choose new password"
                url = '/recover/'+username+'/'+hash_str
                return render_template('new_password.html', message=message, url=url)
    
    if request.method == 'POST':
        if get_pass(username) != None:
            if hash_str == hashlib.md5(username.encode("utf")).hexdigest():
                password = request.form.get('password', '').strip()
                safe_pass = hashlib.md5(password.encode("utf")).hexdigest()
                write_password(username, safe_pass)
                message = "Password changed!"
                return render_template('login.html', message=message)
    
    message = "Password link invalid"
    return render_template('login.html', message=message)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' not in session:
        return render_template('login.html', message="Can't log out! Not logged in")
    session.pop('username', None)
    session.logged_in = False
    session.modified = True 
    return render_template('login.html', message="You have been logged out")

if __name__ == '__main__':
    app.secret_key = '\x8ff\x90T\xc4\xdd\x98d\x8d#'
    app.run(debug=True, use_reloader=True, port=int(web_port))

