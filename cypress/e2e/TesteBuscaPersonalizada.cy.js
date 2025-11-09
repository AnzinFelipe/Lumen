Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('Cesar');
  cy.get('#password').type('123');
  cy.get('button[type="submit"]').click();

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('postarDuasNoticiaseIrNoLeiaMais', () => {
    cy.visit('http://127.0.0.1:8000/criar_noticia/');
    
    cy.get('#titulo').type('Teste de Notícia');
    cy.get('#subtitulo').type('Subtítulo do Teste de Notícia');
    cy.get('#texto').type('Texto do Teste de Notícia');
    cy.get('#autor').type('CesarSchool');
    cy.get('#tema').select('Esportes');
    
    cy.contains('button', 'Criar Notícia').click();
    
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste de Notícia').should('be.visible');
    
    cy.visit('http://127.0.0.1:8000/criar_noticia/');
    
    cy.get('#titulo').type('Teste para o Leia Mais');
    cy.get('#subtitulo').type('Subtítulo do Teste de Leia Mais');
    cy.get('#texto').type('Texto do Teste de Leia Mais');
    cy.get('#autor').type('CesarSchool');
    cy.get('#tema').select('Esportes');
    
    cy.contains('button', 'Criar Notícia').click();

    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste para o Leia Mais').should('be.visible');

    cy.visit('http://127.0.0.1:8000/esportes/');
    cy.contains('Teste de Notícia').should('be.visible');
    cy.contains('Teste de Notícia').click();

    cy.url().should('include', '/noticia_detalhe/');
    
    cy.wait(2000);
    
    cy.contains('Teste para o Leia Mais').should('be.visible');
});

Cypress.Commands.add('ConfirmarBuscaPersonalizada', () => {
    cy.visit('http://127.0.0.1:8000/');
    cy.contains('a', 'Busca personalizada').click();
    cy.url().should('include', 'personalizada/');
    cy.get('h5.card-title').contains('Teste de Notícia').should('be.visible');
});

describe('Fluxo do usuário', () => {
  it('deve criar duas notícias, entrar em uma e depois testar busca personalizada', () => {
    cy.fazerLogin();
    cy.postarDuasNoticiaseIrNoLeiaMais();
    cy.ConfirmarBuscaPersonalizada();
  });
});