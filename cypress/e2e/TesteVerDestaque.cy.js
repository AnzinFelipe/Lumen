Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('Cesar');
  cy.get('#password').type('123');
  cy.get('button[type="submit"]').click();

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('postarTema', () => {
  cy.visit('http://127.0.0.1:8000/criar_noticia/');
  
  cy.get('#id_titulo').type('Teste de Notícia');
  cy.get('#id_subtitulo').type('Subtítulo do Teste de Notícia');
  cy.get('#id_texto').type('Texto do Teste de Notícia');
  cy.get('#id_autor').type('CesarSchool');
  cy.get('#id_tema').select('Esportes');
  
  cy.contains('button', 'Criar Notícia').click();
  
  cy.url().should('eq', 'http://127.0.0.1:8000/');
  cy.contains('Teste de Notícia').should('be.visible');
});

Cypress.Commands.add('verificarNoticiaNosDestaques', () => {
  cy.visit('http://127.0.0.1:8000/');
  
  cy.get('.card-header').contains('Mais Populares').should('be.visible');
  
  cy.get('.card-body').first().within(() => {
    cy.contains('Teste de Notícia').should('be.visible');
  });
});

it('deve criar notícia e checar se ela existe na url do tema e nos destaques', () => {
  cy.fazerLogin();
  cy.postarTema();
  cy.verificarNoticiaNosDestaques();
});