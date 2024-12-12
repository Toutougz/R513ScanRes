from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "bob": generate_password_hash("sponge"),
    "toto": generate_password_hash("tata")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/private')
@auth.login_required
def private():
    return render_template('private.html', user=str.capitalize(auth.current_user()))

if __name__ == '__main__':
    app.run(port=5001,ssl_context=('cert.pem', 'key.pem'))