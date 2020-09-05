import os
from flask import Flask, render_template, session, redirect, url_for, flash, request, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = '41d2bbc19b593add1a0cfaebb3d8bd346f6f279dcc22078c4348a78bdaedddb7'


# a simple page that says hello
@app.route('/')
def landing():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    u = request.form.get('username')
    p = request.form.get('password')
    
    with sqlite3.connect('data.db') as con:
        c = con.cursor()
        c.execute(f'SELECT username, password, level FROM users WHERE username=\'{u}\' and password=\'{p}\'')
        res = c.fetchone()
        if res:
            session['username'] = res[0]
            session['password'] = res[1]
            session['level'] = res[2]
            flash('Login Successful!', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', category='danger')
            return redirect(url_for('landing'))

@app.route('/dashboard')
def dashboard():
    if not session.get('level'):
        return redirect(url_for('landing'))
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    if not session.get('level'):
        return redirect(url_for('landing'))
    with open('templates/profile.html') as f:
        return render_template_string(f.read()
            .replace("%USERNAME%", session.get('username'))
            .replace("%PASSWORD%", session.get('password')))

@app.route('/admin')
def admin():
    if not session.get('level'):
        return redirect(url_for('landing'))
    if session.get('level') != 'admin':
        return render_template('not-admin.html')
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing'))

@app.errorhandler(404)
def not_found(e):
    return render_template('not-found.html'), 404

if __name__ == "__main__":
    app.run()
