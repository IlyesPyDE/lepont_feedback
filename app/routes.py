# Ce fichier contiendra les routes et les vues de notre application Flask
"""
Ce code définit un blueprint nommé "bp" et une route pour la page d'accueil ("/"). 
La route gère à la fois les requêtes GET et POST.

Lorsqu'un formulaire est soumis (requête POST), nous extrayons les données du formulaire,
créons une instance de la classe Feedback (que nous définirons dans "models.py")
et renvoyons un message de succès
Pour les requêtes GET, nous rendons simplement le modèle "index.html"
"""

from flask import Blueprint, render_template,request, redirect, url_for, flash
from .models import Feedback

bp = Blueprint('routes', __name__)

# '/' : Route pour la page d'accueil qui affiche le formulaire de retour et 
#       gère la soumission des nouveaux retours.
@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        formation = request.form['formation']
        feedback_type = request.form['typeRetour']
        date = request.form['date']
        rating = int(request.form['rating'])
        comment = request.form['comments']
        consent = 'consentement' in request.form
        
        if consent:
            feedback = Feedback(formation, feedback_type, date, rating, comment)
            # TODO: Save the feedback data to HDFS

            #
            flash("Merci pour votre contribution ! votre retour a été enregistré.", "success")
        
        return redirect(url_for('routes.home'))
    
    return render_template('index.html')


# '/feedbacks' : Route pour récupérer tous les retours (opération Read).
@bp.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    # TODO: Récupérer tous les retours depuis la base de données (HDFS)
    feedbacks = []
    return render_template('feedbacks.html', feedbacks=feedbacks)

# '/feedbacks/<feedback_id> (GET)' : Route pour récupérer un retour spécifique (opération Read).
@bp.route('/feedbacks/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id):
    # TODO: Récupérer un retour spécifique depuis la base de données (HDFS)
    feedback = None
    return render_template('feedback.html', feedback=feedback)

# '/feedbacks/<feedback_id> (POST)' : Route pour mettre à jour un retour spécifique (opération Update).
@bp.route('/feedbacks/<int:feedback_id>', methods=['POST'])
def update_feedback(feedback_id):
    # TODO: Mettre à jour un retour spécifique dans la base de données (HDFS)
    return redirect(url_for('routes.get_feedback', feedback_id=feedback_id))

# '/feedbacks/<feedback_id> (DELETE)' : Route pour supprimer un retour spécifique (opération Delete).
@bp.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    # TODO: Supprimer un retour spécifique de la base de données (HDFS)
    return '', 204