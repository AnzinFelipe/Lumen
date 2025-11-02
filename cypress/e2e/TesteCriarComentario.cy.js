Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('Cesar');
  cy.get('#password').type('123');
  cy.get('button[type="submit"]').click();

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('criarComentario', () => {
    cy.visit('http://127.0.0.1:8000/criar_noticia/');
    
    cy.get('#id_titulo').type('Teste de Notícia');
    cy.get('#id_subtitulo').type('Subtítulo do Teste de Notícia');
    cy.get('#id_texto').type('Texto do Teste de Notícia');
    cy.get('#id_autor').type('CesarSchool');
    cy.get('#id_tema').select('Esportes');
    
    cy.contains('button', 'Criar Notícia').click();
    
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Ler mais').should('be.visible');
    cy.contains('Ler mais').click();

    cy.url().should('include', '/noticia_detalhe/');
    
    cy.get('.criar_comentario textarea[name="texto"]')
      .should('be.visible')
      .type('comentário teste.');
    
    cy.get('.coment_form button[type="submit"]').click();
    cy.contains('Ler mais').should('be.visible');
    cy.contains('Ler mais').click();

    cy.contains('comentário teste.').should('be.visible');
});

describe('Fluxo do usuário', () => {
  before(() => {
    cy.fazerLogin();
  });

  it('deve criar um comentario', () => {
    cy.criarComentario();
    cy.contains('comentário teste.').should('be.visible');
  });
});