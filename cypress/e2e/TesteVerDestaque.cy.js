Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').clear().type('Cesar');
  cy.get('#password').clear().type('123');
  cy.get('button[type="submit"]').click();

  cy.url().then((url) => {
    if (url.includes('/accounts/login/')) {
      cy.visit('http://127.0.0.1:8000/registrar/');
      cy.get('#username').clear().type('Cesar');
      cy.get('#email').clear().type('cesar@example.com');
      cy.get('#senha').clear().type('123');
      cy.get('#senhaconfirmar').clear().type('123');
      cy.get('button[type="submit"]').click();
      cy.url().should('not.include', '/registrar/');
    }
  });

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('postarTema', () => {
  cy.visit('http://127.0.0.1:8000/criar_noticia/');
  
  cy.get('#titulo').type('Teste de Notícia');
  cy.get('#subtitulo').type('Subtítulo do Teste de Notícia');
  cy.get('#texto').type('Texto do Teste de Notícia');
  cy.get('#autor').type('CesarSchool');
  cy.get('#tema').select('Esportes');
  
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

it('deve criar notícia e checar se ela existe na url dos temas e nos destaques', () => {
  cy.fazerLogin();
  cy.postarTema();
  cy.verificarNoticiaNosDestaques();
});