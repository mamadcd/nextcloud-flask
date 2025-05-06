from flask import Flask, request
import requests

from flask import render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/labs")
def labs():
    return render_template('labs.html')

@app.route('/nextcloud', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        if upload_file(f):
            return "Votre fichier est envoyé dans votre espace nextcloud !"
        else:
            return " l'envoie du fichier a échoué ."
    return render_template('nextcloud.html')
    

def upload_file(file):
    # Remplacez ces valeurs par vos informations d'identification Nextcloud
    nextcloud_url = 'http://your-nextcloud-url'
    username = 'your_username'
    password = 'your_password'

    url = f"{nextcloud_url}/remote.php/webdav/labs/{file.filename}"
    response = requests.put(url, auth=(username, password), data=file.read())

    return response.status_code in [201, 204]
