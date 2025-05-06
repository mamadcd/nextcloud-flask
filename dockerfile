# Utiliser une image de base officielle Python
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /miniprojetcloud

# Copier les fichiers de l'application dans le conteneur
COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Définir la variable d'environnement pour Flask
#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_RUN_PORT=5000
#
# Commande pour exécuter l'application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]