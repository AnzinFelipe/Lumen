Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').clear().type('Cesar');
  cy.get('#password').clear().type('123');
  cy.contains('button', 'ENTRAR').click();

  cy.url().should('not.include', '/accounts/login/');
});

before(() => {
  cy.fazerLogin();
});

Cypress.Commands.add('postarTema', () => {
  cy.contains('a', 'CRIAR NOTÍCIA').click()
  
  cy.get('#titulo').type('Teste de Notícia');
  cy.get('#subtitulo').type('Subtítulo do Teste de Notícia');
  cy.get('#texto').type('Texto do Teste de Notícia');
  cy.get('#autor').type('CesarSchool');
  cy.get('#tema').select('Economia');
  cy.get('input[type="file"]#capa').selectFile('cypress/fixtures/imagem_teste.jpg', { force: true });
  cy.contains('button', 'Criar Notícia').click();
  
  cy.url().should('eq', 'http://127.0.0.1:8000/');
  cy.contains('Teste de Notícia').should('be.visible');
});

Cypress.Commands.add('verificarNoticiaNaPaginaEconomia', () => {
  cy.visit('http://127.0.0.1:8000/');
  
  cy.get('.dropdown-toggle').first().click();
  
  cy.get('.dropdown-menu').should('be.visible');
  cy.get('.dropdown-menu').contains('a', 'Economia').click();
  
  cy.url().should('include', '/economia/');
  
  cy.get('h3').contains('Teste de Notícia').should('be.visible');
  cy.contains('Subtítulo do Teste de Notícia').should('be.visible');
  cy.contains('Por CesarSchool').should('be.visible');
});

it('deve criar notícia e checar se ela existe na página de Economia', () => {
  cy.postarTema();
  cy.verificarNoticiaNaPaginaEconomia();
});