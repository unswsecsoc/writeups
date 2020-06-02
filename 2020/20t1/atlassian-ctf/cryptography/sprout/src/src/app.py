import time
import flask
import config
import base64 as b64
import random
import secrets
import utils
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

app = flask.Flask(__name__)
app.secret_key = secrets.token_bytes(128)

init_posts = [
    {'name': sess['name'], 'content': utils.encrypt(sess['content'], seed=sess['time'])[2], 'time': sess['time']}
    for sess in config.session_config
]


@app.template_filter('b64encode')
def b64encode_filter(content):
    return b64.b64encode(content).decode()


@app.after_request
def security_headers(response):
    # You could add https requirements if you know you will have https
    response.headers['Content-Security-Policy'] = "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self';"
    response.headers['X-Content-Type-Options'] = "nosniff"
    return response


@app.route('/encrypt', methods=["POST"])
def encrypt():
    key, iv, content = utils.encrypt(flask.request.form['content'])
    return flask.jsonify({'name': flask.request.form['name'], 'content': b64.b64encode(content).decode(), 'time': utils.get_time(), 'key': b64.b64encode(iv + key).decode()})


@app.route('/', methods=["GET"])
def index():
    return flask.render_template('index.html', posts=init_posts)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
