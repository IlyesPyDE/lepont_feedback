describe('Feedback Tests', () => {
    beforeEach(() => {
        // Visitez la page d'accueil avant chaque test
        cy.visit('http://localhost:5000');
    });

    it('should submit a feedback', () => {
        //Remplissez le formulaire de feedback
        cy.get('select[name="formation"]').select('data_engineering');
        cy.get('select[name="typeRetour"]').select('contenu_cours');
        cy.get('input["date"]').type('2023-05-29');
        cy.get('input[name="rating"]').type('4');
        cy.get('textarea[name="comments"]').type('cours interessant');
        ...
    }
)