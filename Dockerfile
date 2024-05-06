# Utiliser une image Python comme image de base 
FROM python:3.12

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


# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]