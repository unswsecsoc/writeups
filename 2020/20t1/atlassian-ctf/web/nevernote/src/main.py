import sqlite3
import random
import string
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, make_response, flash

FLAG = os.getenv('FLAG', 'ATLASSIAN{d0nt_wR8te_sQ!_lk_dis_pl0x_504e0b706a32}')

def random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))

# initialise memory database
db = sqlite3.connect(':memory:', check_same_thread=False)


c = db.cursor()
c.execute('''CREATE TABLE notes
             (id text, title text, content text)''')
c.execute('INSERT INTO notes (id, title, content) VALUES (?,?,?)', (random_id(), 'flag', 'ATLASSIAN{sorry_this_is_not_the_flag}'))
c.execute('INSERT INTO notes (id, title, content) VALUES (?,?,?)', (random_id(), 'flag?', 'ATLASSIAN{look_a_bit_harder_also_not_flag}'))
c.execute('''CREATE TABLE config
             (key text, value text, UNIQUE(key))''')
c.execute('INSERT INTO config (key, value) VALUES(?,?)',('mysql_username', 'root'))
c.execute('INSERT INTO config (key, value) VALUES(?,?)',('mysql_password', 'welcome1'))
c.execute('INSERT INTO config (key, value) VALUES(?,?)',('clearly this', 'isn\'t legit'))
c.execute('INSERT INTO config (key, value) VALUES(?,?)',('flag', FLAG))
c.close()


app = Flask(__name__,
            static_folder = './templates',
            template_folder = './templates')

app.secret_key = secrets.token_urlsafe(32)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/new', methods=['POST'])
def new_note():
    cl = request.content_length
    if cl is not None and cl > 32 * 1024:
        flash("request too big")
        redirect("/")

    title = request.form.get('title', '')
    content = request.form.get('content', '')

    if title == '' or content == '':
        flash('please complete all fields')
        return redirect('/')

    note_id = random_id()
    c = db.cursor()
    c.execute('INSERT INTO notes (id, title, content) VALUES(?, ?, ?)', (note_id, title, content))
    c.close()
    return redirect(f'/note?id={note_id}')

@app.route('/note', methods=['GET'])
def view_note():
    note_id = request.args.get('id', default='0')
    try:
        c = db.cursor()
        # this is where error is
        c.execute(f'SELECT title, content FROM notes WHERE id=\'{note_id}\'')
        res = c.fetchone()
        c.close()
        if res == None:
            flash('note doesn\'t exist :(')
            return redirect('/')

        return render_template('note.html', id=note_id, title=res[0], content=res[1])
    except:
        flash('note doesn\'t exist :(')
        return redirect('/')



if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')

