# Ce fichier contiendra les routes et les vues de notre application Flask
"""
Ce code définit un blueprint nommé "bp" et une route pour la page d'accueil ("/"). 
La route gère à la fois les requêtes GET et POST.

Lorsqu'un formulaire est soumis (requête POST), nous extrayons les données du formulaire,
créons une instance de la classe Feedback (que nous définirons dans "models.py")
et renvoyons un message de succès
Pour les requêtes GET, nous rendons simplement le modèle "index.html"
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Feedback
import csv
from pywebhdfs.webhdfs import PyWebHdfsClient
from pyhive import hive


bp = Blueprint('routes', __name__)

# '/' : Route pour la page d'accueil qui affiche le formulaire de retour et 
#       gère la soumission des nouveaux retours.
@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        bootcamp = request.form['formation']
        feedback_type = request.form['typeRetour']
        date = request.form['date']
        rating = int(request.form['rating'])
        comment = request.form['comments']
        consent = 'consentement' in request.form
        
        if consent:
            feedback = Feedback(bootcamp, feedback_type, date, rating, comment)

            try:
                # Écrire les données dans HDFS
                hdfs = PyWebHdfsClient(host='localhost', port='50070', user_name='hdfs')
                hdfs.create_file('/user/hdfs/feedbacks.csv', f"{bootcamp},{feedback_type},{date},{rating},'{comment}'\n", append=True)

                # Insérer les données dans Hive
                conn = hive.Connection(host="localhost", port=10000, database="default")
                cursor = conn.cursor()

                query = f"INSERT INTO feedbacks (bootcamp, feedback_type, date, rating, comment) VALUES ('{bootcamp}', '{feedback_type}', '{date}', {rating}, '{comment}')"
                cursor.execute(query)

                conn.close()

                # créer un message Flash 
                flash("Merci pour votre contribution ! votre retour a été enregistré.", "success")             
                
            except Exception as e:
                print(f"Erreur lors de l'enregistrement du feedback : {str(e)}")
                flash("Une erreur est survenue. Veuillez réessayer plus tard.", "danger")                      

                    
        return redirect(url_for('routes.home'))
    
    return render_template('index.html')




# '/feedbacks' : Route pour récupérer tous les retours (opération Read).
@bp.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    # Récupérer tous les retours depuis la base de données (HDFS)
    try:
        conn = hive.Connection(host="localhost", port=10000, database="default")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedbacks")
        feedbacks = cursor.fetchall()
        conn.close()
        return render_template('feedbacks.html', feedbacks=feedbacks)
    
    except Exception as e:
        print(f"Erreur lors de la récupération des feedbacks depuis Hive : {str(e)}")
        flash("Une erreur est survenue. Veuillez réessayer plus tard.", "danger")
        return render_template('feedbacks.html', feedbacks=[])
    

    
# '/feedbacks/<id> (GET)' : Route pour récupérer un retour spécifique (opération Read).
@bp.route('/feedbacks/<int:id>', methods=['GET'])
def get_feedback(id):
    # Récupérer un retour spécifique depuis la base de données (HDFS)
    try:
        conn = hive.Connection(host="localhost", port=10000, database="default")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM feedbacks WHERE id = {id}")
        feedback = cursor.fetchone()
        conn.close()
        if feedback:
            return render_template('feedback.html', feedback=feedback)
        else:
            flash(f"Le feedback avec l'ID {id} n'a pas été trouvé.", "warning")
            return redirect(url_for('routes.get_feedbacks'))
        
    except Exception as e:
        print(f"Erreur lors de la récupération du feedback depuis Hive : {str(e)}")
        flash("Une erreur est survenue. Veuillez réessayer plus tard.", "danger")
        return redirect(url_for('routes.get_feedbacks'))
    


# '/feedbacks/<feedback_id> (POST)' : Route pour mettre à jour un retour spécifique (opération Update).
@bp.route('/feedbacks/<int:id>', methods=['POST'])
def update_feedback(id):
    # Mettre à jour un retour spécifique dans la base de données (HDFS)
    bootcamp = request.form['formation']
    feedback_type = request.form['typeRetour']
    date = request.form['date']
    rating = int(request.form['rating'])
    comment = request.form['comments']

    try:
        conn = hive.Connection(host="localhost", port=10000, database="default")
        cursor = conn.cursor()
        
        query = f"UPDATE feedbacks SET bootcamp = '{bootcamp}', feedback_type = '{feedback_type}', date = '{date}', rating = {rating}, comment = '{comment}' WHERE id = {id}"
        cursor.execute(query)
        
        conn.close()
        
        flash(f"Le feedback avec l'ID {id} a été mis à jour.", "success")

    except Exception as e:
        print(f"Erreur lors de la mise à jour du feedback dans Hive : {str(e)}")
        flash("Une erreur est survenue. Veuillez réessayer plus tard.", "danger")

    return redirect(url_for('routes.get_feedback', id=id))

    

# '/feedbacks/<id> (DELETE)' : Route pour supprimer un retour spécifique (opération Delete).
@bp.route('/feedbacks/<int:id>', methods=['DELETE'])
def delete_feedback(id):
    # Supprimer un retour spécifique de la base de données (HDFS)
    try:
        conn = hive.Connection(host="localhost", port=10000, database="default")
        cursor = conn.cursor()
        
        query = f"DELETE FROM feedbacks WHERE id = {id}"
        cursor.execute(query)
        
        conn.close()

        flash(f"Le feedback avec l'ID {id} a été supprimé.", "success")

    except Exception as e:
        print(f"Erreur lors de la suppression du feedback dans Hive : {str(e)}")
        flash("Une erreur est survenue. Veuillez réessayer plus tard.", "danger")

    return '', 204