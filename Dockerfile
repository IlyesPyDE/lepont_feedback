# Utiliser une image Python comme image de base 
FROM python:3.12

# Ajouter des méradonnées avec l'instruction LABEL ## Pas nécessaire mais best practice
LABEL maintainer="Ilyes"
LABEL description="Application Flask pour les retours de formation"

# Définir des variables d'environnement avec l'instruction ENV ## pas nécessaire mais best practice
ENV FLASK_APP=app.py
ENV FLASK_ENV=dev

# Définir le répertoire de travail dans le conteneur
# Tous les fichiers copiés et les commandes exécutées se feront dans ce répertoire
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY requirements.txt .
COPY app app 
COPY app.py .

# Installer les dépendances Python 
# Les packages flask, pyhive et pywebhdfs sont installés avec pip
RUN pip install --no-cache-dir -r requirements.txt

# Créer un utilisateur non-rout pour exécuter l'application ## pas nécessaire mais BEST practice
RUN useradd -ms /bin/bash appuser
USER appuser

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]



### Commandes pour construire l'image Docker
# docker build -t lepont-feedback .
# docker run -p 5000:5000 lepont-feedback

## vérification que l'application Flask s'exécute correctement dans le conteneur Docker
# http://localhost:5000