from flask import Flask, render_template,  flash, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory


UPLOAD_FOLDER = './uploads/web'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'tototatatiti'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Fichier téléversé avec succes')
            return redirect(url_for('upload_file', name=filename))
        # pour aller plus loin:
        # https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(port=5001,ssl_context=('cert.pem', 'key.pem'))