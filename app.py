# Ce code crée une application Flask et enregistre un "blueprint" -
# - (que nous définirons dans "routes.py") pour gérer les routes de l'application.

from flask import Flask

from app import create_app 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)