import config
import flask
import functools
import os, os.path
import hashlib
import string

app = flask.Flask(__name__, template_folder="fs_templates")

def local_network(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if flask.request.remote_addr != "127.0.0.1":
            return 'This functionality is not avaliable publicly. (Staff should login to the server to use it)', 403
        else:
            return fn(*args, **kwargs)
    return wrapper

def requires_token(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        token = flask.request.args.get('token')
        TOKEN_CHARSET = string.ascii_letters + string.digits
        if token is None or len(token) == 0:
            return 'Missing token', 400
        if len(token) < 48 or any(t not in TOKEN_CHARSET for t in token):
            # Token must be alphanumeric and at least len 48
            return 'Invalid token (token must be alphanumeric and at least length 48).' +\
                   ' Please try to pick something unique in order to prevent other people viewing your answers.' + \
                   ' <i>This is a genuine suggestion and not part of the challenge.</i>'+\
                   '<br>Suggestion: ' + "".join(TOKEN_CHARSET[i % len(TOKEN_CHARSET)] for i in os.urandom(64)), 400
        return fn(*args, **kwargs)
    return wrapper


def make_dir_name(token):
    return os.path.join(config.file_dir, hashlib.sha1(token.encode() + config.dir_secret.encode()).hexdigest())


@app.route('/', methods=["GET"])
@requires_token
def list_files():
    token = flask.request.args.get('token')
    sess_dir = make_dir_name(token)

    files = []
    if os.path.isdir(sess_dir):
        files = [f for f in os.listdir(sess_dir) if os.path.isfile(os.path.join(sess_dir, f))]

    return flask.render_template('list.html', files=files, token=token)

@app.route('/favicon.ico')
def no_favicon(): return "", 404

@app.route('/<loc>', methods=["GET"])
@requires_token
def get_file(loc):
    token = flask.request.args.get('token')
    sess_dir = make_dir_name(token)

    if not os.path.isdir(sess_dir):
        return "This token has no associated directory (note PUTting a file will automatically create one)", 404

    return flask.send_from_directory(sess_dir, loc)  # Handles path traversal sanitization for us

@app.route('/<loc>', methods=["PUT"])
@local_network
@requires_token
def put_file(loc):
    token = flask.request.args.get('token')
    sess_dir = make_dir_name(token)

    if not os.path.isdir(sess_dir):
        os.mkdir(sess_dir)

    file_loc = flask.safe_join(sess_dir, loc)
    with open(file_loc, 'wb') as f:
        f.write(flask.request.data)
    return flask.jsonify({'disk': file_loc})

@app.route('/<loc>', methods=["DELETE"])
@local_network
@requires_token
def delete_file(loc):
    token = flask.request.args.get('token')
    sess_dir = make_dir_name(token)

    if not os.path.isdir(sess_dir):
        return "This token has no associated directory", 404

    file_loc = flask.safe_join(sess_dir, loc)
    if not os.path.isfile(file_loc):
        return "404 Not Found", 404

    os.unlink(file_loc)
    return file_loc

if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")
