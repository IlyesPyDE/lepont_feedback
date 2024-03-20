from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    formation = request.form.get('formation')
    priorite = request.form.get('priorit')
    type_retour = request.form.get('type_retour')
    date = request.form.get('date')
    evaluation = request.form.get('evaluation')
    commentaires = request.form.get('commentaires')

    feedbacks = []
    feedback = {
    'formation': formation,
    'priorite': priorite,
    'type_retour': type_retour,
    'date': date,
    'evaluation': evaluation,
    'commentaires': commentaires
    }

    feedbacks.append(feedback)

    return render_template('confirmation.html',
                           formation=formation,
                           priorite=priorite,
                           type_retour=type_retour,
                           date=date,
                           evaluation=evaluation,
                           commentaires=commentaires)






if __name__ == '__main__':
    app.run()