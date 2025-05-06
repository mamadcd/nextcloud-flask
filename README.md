# Documentation Technique : Lancer le Projet Flask avec Docker

Ce document explique comment configurer, construire et exécuter une application Flask intégrée avec Nextcloud en utilisant Docker.

## Prérequis

- Docker et Docker Compose installés sur votre machine.
- Accès à un terminal de commande.

## Structure du Projet

Le projet est structuré comme suit :

miniprojetcloud/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── templates/
├── index.html
├── labs.html
├── nextcloud.html
└── static/
├── style.css

## Configuration

### Fichier `app.py`

Configurez les paramètres de connexion à votre instance Nextcloud dans le fichier `config.py` :

```python
Modifiez La fonction
def upload_file(file):
    nextcloud_url = 'http://your-nextcloud-url'  # Remplacez par l'URL de votre serveur Nextcloud
    username = 'your_username'                   # Votre nom d'utilisateur Nextcloud
    password = 'your_password'                   # Votre mot de passe Nextcloud
```

## Construction et Exécution avec Docker

Se mettre dans le répertoire de base de l'application et ouvrer le terminal
Dans le répertoire racine du projet, exécutez la commande suivante pour construire les images Docker définies dans le Dockerfile :

- docker-compose build

Une fois les images construites, démarrez les services définis dans le fichier docker-compose.yml :

- docker-compose up

Stoper les services avec :

- docker-compose down

## Accéder à l'Application
Application Flask : 
- Ouvrez votre navigateur et accédez à http://localhost:5000 pour voir votre application Flask en cours d'exécution.
Nextcloud :
- Accédez à http://localhost:8080 pour configurer et utiliser Nextcloud.

## captures dans le fichier pdf capture.pdf
