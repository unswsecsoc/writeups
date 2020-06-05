from flask import Flask, request, render_template
import qswt
import secrets
import os

FLAG = os.getenv('FLAG', 'ATLASSIAN{h3sh_L3ngth_XXXtension_8ttack_f288b6acf6b1}')
SECRET = secrets.token_bytes(32)
app = Flask(__name__, static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 86400

@app.route('/')
def home():
    return render_template('home.html', login_qswt=qswt.encode({'username': 'user', 'nonce': secrets.token_hex(4)}, SECRET))

@app.route('/dashboard')
def dashboard():
    token = request.args.get('qswt', '')
    if not qswt:
        return render_template('error.html', message="Authentication failed: Invalid QSWT"), 400
    data = qswt.decode(token, SECRET)
    if not data:
        return render_template('error.html', message="Authentication failed: Invalid QSWT"), 400

    if data['username'] == 'admin':
        return render_template('dashboard.html', username=data['username'], flag=FLAG)
    
    return render_template('dashboard.html', username=data['username'])


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', message="Page not found"), 404

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')

