# tests/test_routes.py
# NOTE: utiliser la commande : "python -m pytest" pour lancer le test au lieu de "pytest tests" 

import pytest
from app import create_app

# Le décorateur @pytest.fixture crée une fonction qui sera exécutée avant chaque test.
# Cette fonction crée une instance de l'application Flask et un client de test.
@pytest.fixture
def client():
    # Crée une instance de l'application Flask en appelant la fonction create_app().
    app = create_app()
    # Configure l'application pour le mode de test.
    app.config["TESTING"] = True
    # Crée un client de test pour envoyer des requêtes HTTP à l'application.
    with app.test_client() as client:
        # Utilise yield au lieu de return pour que le client reste accessible après l'exécution du test.
        yield client


# Définit un test pour la route de la page d'accueil ("/").
def test_home_route(client):
    # Envoie une requête GET à la route "/".
    response = client.get("/")
    # Vérifie que le code de statut de la réponse est 200 (OK).
    assert response.status_code == 200
    # Vérifie que la réponse contient le texte "Votre retour sur la formation".
    assert b"Votre retour sur la formation" in response.data


# Définit un test pour la soumission d'un feedback via le formulaire.
def test_submit_feedback(client):
    # Crée un dictionnaire contenant les données du formulaire à soumettre.
    data = {
        "formation": "data_engineering",
        "typeRetour": "contenu_cours",
        "date": "2024-04-29",
        "rating": 6,
        "comments": "bon cours.",
        "consentement": True
    }
    # Envoie une requête POST à la route "/" avec les données du formulaire.
    response = client.post("/", data=data)
    # Vérifie que le code de statut de la réponse est 302 (redirection).
    assert response.status_code == 302
    # Vérifie que la redirection se fait vers la page d'accueil ("/").
    assert response.location.endswith("/")


# Définit un test pour la récupération de tous les feedbacks.
def test_get_feedbacks(client):
    # Envoie une requête GET à la route "/feedbacks".
    response = client.get("/feedbacks")
    # Vérifie que le code de statut de la réponse est 200 (OK).
    assert response.status_code == 200
    # Vérifie que la réponse contient le texte "Liste des retours".
    assert b"Liste des retours" in response.data


# Définit un test pour la récupération d'un feedback spécifique.
def test_get_feedback(client):
    # Supposons que le feedback avec l'ID 55 existe.
    # Envoie une requête GET à la route "/feedbacks/55".
    response = client.get("/feedbacks/55")
    # Vérifie que le code de statut de la réponse est 200 (OK).
    assert response.status_code == 200
    # Vérifie que la réponse contient le texte "Détails du retour".
    assert "Détails du retour" in response.data.decode('utf-8')


# Définit un test pour la mise à jour d'un feedback spécifique.
def test_update_feedback(client):
    # Crée un dictionnaire contenant les données du formulaire de mise à jour.
    data = {
        "formation": "data_engineering",
        "typeRetour": "contenu_cours",
        "date": "2024-05-01",
        "rating": 7,
        "comments": "Excellent cours, très instructif."
    }
    # Envoie une requête POST à la route "/feedbacks/55/update" avec les données de mise à jour.
    response = client.post("/feedbacks/55/update", data=data)
    # Vérifie que le code de statut de la réponse est 302 (redirection).
    assert response.status_code == 302
    # Vérifie que la redirection se fait vers la page de détails du feedback avec l'ID 55.
    assert response.location.endswith("/feedbacks/55")


# Définit un test pour la suppression d'un feedback spécifique.
def test_delete_feedback(client):
    # Envoie une requête DELETE à la route "/feedbacks/55".
    response = client.delete("/feedbacks/55")
    # Vérifie que le code de statut de la réponse est 204 (pas de contenu).
    assert response.status_code == 204