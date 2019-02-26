import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def route_index():
    auth = request.cookies.get('auth')
    if auth is not None and auth == get_auth():
        return render_template('index.html', flag=get_flag())

    return redirect(url_for('route_login', error='unauthenticated'))


@app.route('/login', methods=['GET', 'POST'])
def route_login():
    auth = request.cookies.get('auth')
    if auth == get_auth():
        return redirect(url_for('route_index'))

    with sqlite3.connect(":memory:") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS app_users "
                  "(user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);")
        c.execute("INSERT OR IGNORE INTO app_users (username, password) "
                  "VALUES ('admin', 'you_will_never_guess_this');")

        if request.method == 'POST':
            query = "SELECT * FROM app_users WHERE username = '{}' AND password = '{}';".format(
                request.form.get('inputUsername'),
                request.form.get('inputPassword'))
            try:
                c.execute(query)
            except sqlite3.Error as e:
                return render_template('error.html', sql_query=query, sql_error=str(e))

            result = c.fetchone()

            if result is not None:
                resp = redirect(url_for('route_index'))
                resp.set_cookie('auth', get_auth(), max_age=10)
                return resp
            else:
                return redirect(url_for('route_login', error='incorrect'))

        return render_template('login.html')


def get_auth() -> str:
    with open('secrets/auth') as f:
        return f.read().strip()


def get_flag() -> str:
    with open('secrets/flag') as f:
        return f.read().strip()
