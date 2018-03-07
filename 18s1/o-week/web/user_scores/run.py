from flask import Flask, render_template, request, g, session, redirect, abort
import time
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'B3Dvm1BJF1'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        conn = sqlite3.connect('db.sqlite')
        searchRequest = request.form["search"]
        if re.search('delete', searchRequest.lower()) or re.search('drop', searchRequest.lower()):
            return render_template('dickhead.html')
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        data = c.execute("SELECT * FROM SCORES WHERE USER LIKE \'"+searchRequest+"\'").fetchall()
        conn.close()
        return render_template('index.html',t=str(time.time()),scores=data)
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    test = c.execute("SELECT * FROM SCORES").fetchall()
    conn.close()
    return render_template('index.html',t=str(time.time()),scores=test)

if __name__ == "__main__":
	app.run(debug=True)
