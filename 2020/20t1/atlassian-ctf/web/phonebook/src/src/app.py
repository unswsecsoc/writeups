import string
import sqlite3
from flask import Flask, render_template, jsonify, request, session
import secrets
import config
import time

# TODO: add check for localhost admin access

app = Flask(__name__)
app.config['SECRET_KEY'] = str(secrets.randbits(1024))

MAX_NUMS = 192

def query_db(query, args=[], lri=False):
    with sqlite3.connect('phonenumbers.db') as db:
        cur = db.execute(query, args)
        rv  = cur.fetchall()
        lii = cur.lastrowid
        cur.close()
        return (rv, lii) if lri else rv

def get_name(pbid):
    return query_db('SELECT name FROM phonebooks WHERE id = ?', [pbid])[0][0]

def get_entries(pbid):
    return query_db('SELECT phonenumber, numberowner FROM phonenumbers WHERE pbid = ?', [pbid])

def get_messages(pbid):
    return query_db('SELECT message FROM messages WHERE pbid = ?', [pbid])

def owns(pbid, sessid):
    if 'flag' in request.cookies and request.cookies['flag'] == config.FLAG:
        return True
    return any(str(i[0]) == str(pbid) for i in query_db('SELECT id FROM phonebooks WHERE user_id = ?', [sessid]))

def consumed_space(pbid):
    return query_db('SELECT count(*) FROM phonenumbers WHERE pbid = ?', [pbid])[0][0] == MAX_NUMS

@app.route('/api/admin/message', methods=["POST"])
def message():
    if 'flag' not in request.cookies or request.cookies['flag'] != config.FLAG:
        return 'This API is for administrators only', 403
    if 'referer' not in request.headers:
        return '', 400

    referer = request.headers['referer']
    try:    pbid = int(referer.split('/')[-1])
    except: return '', 400

    query_db('INSERT INTO messages(pbid, message) VALUES (?, ?)', [pbid, request.json['message']])
    return jsonify({'success': True})


@app.route('/api/phonebook', methods=["POST"])
def new_phonebook():
    if 'id' not in session: session['id'] = hex(secrets.randbits(1024))[2:]

    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + "{}[]<>!@#$%^&*()/"
    pbname = request.json['pbname'][:10]

    if any(c not in allowed_chars for c in pbname):
        return '"Found illegal character: phonebook names must be in ' + allowed_chars + '"', 400

    _, lid = query_db('INSERT INTO phonebooks(name, user_id, created) VALUES (?, ?, ?)', [pbname, session['id'], int(time.time())], lri=True)
    return jsonify(lid), 200

@app.route('/api/phonebook/<pbid>', methods=["PUT", "POST"])
def add_phonebook_entry(pbid):
    if 'id' not in session: session['id'] = hex(secrets.randbits(1024))[2:]
    if not owns(pbid, session['id']): return '"You do not own that bin"', 400

    banned_chars = string.ascii_letters + '`'
    phonenumber = request.json['phonenumber'][:7]
    numberowner = request.json['numberowner']

    if consumed_space(pbid):
        return '"We only support up to '+ str(MAX_NUMS)+' entries (start a new bin if you need to try again - this bin will automatically be deleted)"', 400

    if any(c in banned_chars for c in phonenumber):
        return '"Found banned character. There must not be any letters [a-zA-Z`]"', 400

    query_db('INSERT INTO phonenumbers(pbid, phonenumber, numberowner) VALUES (?, ?, ?)',
             [pbid, phonenumber, numberowner])
    return "1", 200

@app.route('/phonebook/<pbid>')
def show_phonebook(pbid):
    if 'id' not in session: session['id'] = hex(secrets.randbits(1024))[2:]
    if not owns(pbid, session['id']): return 'You do not own that bin', 400

    name = get_name(pbid)
    book = get_entries(pbid)
    msgs = get_messages(pbid)

    return render_template('phonebook.html', name=name, numbers=book, messages=msgs)

@app.route('/')
def index():
    if 'id' not in session: session['id'] = hex(secrets.randbits(1024))[2:]
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
