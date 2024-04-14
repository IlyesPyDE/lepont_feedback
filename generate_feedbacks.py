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