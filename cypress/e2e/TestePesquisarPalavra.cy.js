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
  
  cy.get('#titulo').type('Brasil entra em crise');
  cy.get('#subtitulo').type('Subtítulo do Teste de Notícia');
  cy.get('#texto').type('Texto do Teste de Notícia');
  cy.get('#autor').type('CesarSchool');
  cy.get('#tema').select('Esportes');
  
  cy.contains('button', 'Criar Notícia').click();
  
  cy.url().should('eq', 'http://127.0.0.1:8000/');
  cy.contains('Teste de Notícia').should('be.visible');
});

Cypress.Commands.add('PesquisarPalavra', () => {
    cy.get('input[placeholder="Pesquisar notícias"]').type('crise');
    cy.get('button[type="submit"]').click();
    cy.wait(2000);
    cy.contains('Brasil entra em crise').should('be.visible'); 

});

it('deve criar notícia e checar se ela está visível ao pesquisar palavra chave', () => {
  cy.fazerLogin();
  cy.postarTema();
  cy.PesquisarPalavra();
});