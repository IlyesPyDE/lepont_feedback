# Ce fichier contiendra les modèles de données de notre application.

# Ce code définit une classe Feedback qui représente un retour d'apprenant

class Feedback:
    def __init__(self, formation, feedback_type, date, rating, comment):
        self.formation = formation
        self.feedback_type = feedback_type
        self.date = date
        self.rating = rating
        self.comment = comment      