# Methode pour générer des feedbacks en csv "feedbacks.csv"

import csv
import random
from datetime import datetime, timedelta

# Définition des données
bootcamps = ['data_engineering', 'data_science', 'web_development', 'cyber_security', 'artificial_intelligence', 'cloud_computing']
feedback_types = ['contenu_cours', 'formateur', 'methodes_pedagogiques', 'support_cours', 'environnement_apprentissage', 'communication', 'axe_amelioration']
comments = {
    'cloud_computing': {
        'formateur': ["Formateur compétent", "Formateur très compétent"],
        'contenu_cours': ["Cours corrects mais manque de pratique"],
        'default': [
            "Ressources complémentaires limitées", "Nécessite plus de pratique", "Environnement d'apprentissage peu stimulant",
            "Bonne communication", "Méthodes pédagogiques correctes mais manque de pratique", "Ressources complémentaires de mauvaise qualité"
        ]
    },
    'default': [
        "Contenu moyen, manque de profondeur", "Formateur peu expérimenté", "Méthodes pédagogiques à revoir",
        "Support de cours insuffisant", "Environnement d'apprentissage peu stimulant", "Communication limitée",
        "Nécessite des améliorations significatives", "Cours trop théorique, manque de pratique", "Ressources complémentaires limitées",
        "Méthodes pédagogiques peu adaptées", "Formateur manquant de dynamisme", "Environnement d'apprentissage bruyant",
        "Communication peu claire", "Nécessite une refonte du programme", "Contenu peu innovant",
        "Support de cours incomplet", "Méthodes pédagogiques ennuyeuses", "Formateur peu disponible",
        "Environnement d'apprentissage inconfortable", "Communication inefficace", "Nécessite plus de pratique",
        "Cours trop dense", "Ressources complémentaires de mauvaise qualité", "Méthodes pédagogiques inadaptées",
        "Formateur peu pédagogue", "Environnement d'apprentissage démotivant", "Communication impersonnelle"
    ]
}

# Génération des données aléatoires
data = []
start_date = datetime(2023, 5, 1)
end_date = datetime(2023, 12, 4)

for _ in range(50):
    bootcamp = random.choice(bootcamps)
    feedback_type = random.choice(feedback_types)
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Génération des notes avec une probabilité plus élevée pour les notes 4 et 5
    rating_probabilities = [0.1, 0.2, 0.3, 0.3, 0.1]
    rating = random.choices([3, 4, 5, 6, 7], weights=rating_probabilities)[0]
    
    if bootcamp == 'cloud_computing' and feedback_type in comments['cloud_computing']:
        comment = random.choice(comments['cloud_computing'][feedback_type])
    else:
        comment = random.choice(comments['default'])
    
    data.append([bootcamp, feedback_type, date.strftime("%Y-%m-%d"), rating, comment])

# Écriture des données dans un fichier CSV
with open('feedback_data_updated.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['bootcamp', 'feedback_type', 'date', 'rating', 'comment'])
    writer.writerows(data)

print("Le fichier CSV mis à jour a été généré avec succès.") 





'''
import csv
import random
from datetime import datetime, timedelta

# Définition des données possible pour chaque champ
bootcamps = ['data_engineering', 'data_science', 'web_development', 'cyber_security', 'artificial_intelligence', 'cloud_computing']
feedback_types = ['contenu_cours', 'formateur', 'methodes_pedagogiques', 'support_cours', 'environnement_apprentissage', 'communication', 'axe_amelioration']

# Commentaires liés aux plages de notes
ratings_comments = {
    (0, 1): "à fuir",
    (2, 3): "plutôt mauvais",
    (4, 5): "moyen",
    (6, 7): "pas mal",
    (8, 9): "très bon",
    (10, 10): "excellent"
}

# Fonction pour générer une date aléatoire entre deux bornes
def random_date(start, end):
    return (start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))).strftime('%d/%m/%Y')

start_date = datetime.strptime('04/12/2023', '%d/%m/%Y')
end_date = datetime.strptime('30/03/2024', '%d/%m/%Y')

# Création du fichier CSV
with open('feedbacks.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['bootcamp', 'feedback_type', 'date', 'rating', 'comment'])
    
    for _ in range(50):
        bootcamp = random.choice(bootcamps)
        feedback_type = random.choice(feedback_types)
        date = random_date(start_date, end_date)
        rating = random.randint(0, 10)  # Génération d'une note aléatoire entre 0 et 10
        comment = next(comment for range_, comment in ratings_comments.items() if range_[0] <= rating <= range_[1])
        
        writer.writerow([bootcamp, feedback_type, date, rating, comment])

print("Fichier CSV généré avec succès.")

'''