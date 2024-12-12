from flask import Flask, render_template
from flask_httpauth import HTTPDigestAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "bob": "sponge",
    "toto": "tata"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/private')
@auth.login_required
def private():
    return render_template('private.html', user=str.capitalize(auth.current_user()))

if __name__ == '__main__':
    app.run()