import time
import uuid
import flask
import secrets
import sqlite3
import hashlib

app = flask.Flask(__name__)
app.secret_key = secrets.token_bytes(128)

def query_db(query, args=[]):
    with sqlite3.connect('cms.db') as db:
        cur = db.execute(query, args)
        rv  = cur.fetchall()
        cur.close()
        return rv

def prepare_template(template):
    return """
    <!doctype html>
    <html>
        <head><title>CMS | {{ title }}</title></head>
        <body>
            <div>
                <header></header>
                <main>
                    <h1>{{ title }}</h1>
                    <div>""" + template + """</div>
                </main>
            </div>
    </html>
    """

@app.context_processor
def context():
    return {'time': lambda: time.strftime("%X"), 'date': lambda: time.strftime("%x")}

@app.route('/')
@app.route('/<page_route>')
def get_page(page_route=''):
    page = query_db(f"SELECT title, template, auth FROM pages WHERE route = '{page_route}';")
    if len(page) == 0:
        return '404 Not Found', 404

    page = page[0]
    tmpl = page[1]
    auth = page[2]

    if auth is not None:
        if 'token' not in flask.request.args:
            return 'Missing ?token', 400
        if flask.request.args['token'] != auth:
            return 'Invalid token', 403

    return flask.render_template_string(prepare_template(page[1]), title=page[0], auth=auth)

@app.route('/api/page', methods=["POST"])
def make_page():
    if not all(ki in flask.request.form for ki in ('token', 'title', 'template', 'auth')):
        return 'Invalid Arguments', 400

    token = flask.request.form['token']
    if query_db('SELECT count(*) FROM pages WHERE auth=?', [token])[0] == '0':
        return 'The supplied token is invalid', 403

    if '|' not in token or token.split('|')[1] != 'admin':
        return 'Only admin tokens can make new pages', 403

    prefix = hashlib.sha1(str(uuid.uuid4()).encode()).hexdigest()
    query_db('INSERT INTO pages(route, title, template, auth) VALUES (?, ?, ?, ?)', [
        prefix + flask.request.form['route'],
        flask.request.form['title'],
        flask.request.form['template'],
        flask.request.form['auth'] if len(flask.request.form['auth']) > 0 else None
    ])

    return prefix + flask.request.form['route'], 200

if __name__ == '__main__':
    app.run(port=5000)
