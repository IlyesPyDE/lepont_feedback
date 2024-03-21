from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Récupération des données du formulaire
    formation = request.form.get('formation')
    priorite = request.form.get('priorit')
    type_retour = request.form.get('type_retour')
    date = request.form.get('date')
    evaluation = request.form.get('evaluation')
    commentaires = request.form.get('commentaires')

    # Création de la liste feedbacks à l'intérieur de la fonction
    feedbacks = []

    # Création d'un dictionnaire avec les données du formulaire
    feedback = {
    'formation': formation,
    'priorite': priorite,
    'type_retour': type_retour,
    'date': date,
    'evaluation': evaluation,
    'commentaires': commentaires
    }

    # Ajout du dictionnaire à la liste
    feedbacks.append(feedback)

    # Renvoyer le template de confirmation
    return render_template('confirmation.html',
                           formation=formation,
                           priorite=priorite,
                           type_retour=type_retour,
                           date=date,
                           evaluation=evaluation,
                           commentaires=commentaires)






if __name__ == '__main__':
    app.run(debug=True)