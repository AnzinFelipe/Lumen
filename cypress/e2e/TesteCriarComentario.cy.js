Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('Cesar');
  cy.get('#password').type('123');
  cy.contains('button', 'ENTRAR').click();

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('criarComentario', () => {
    cy.contains('a', 'CRIAR NOTÍCIA').click()
    
    cy.get('#titulo').type('Teste de Notícia');
    cy.get('#subtitulo').type('Subtítulo do Teste de Notícia');
    cy.get('#texto').type('Texto do Teste de Notícia');
    cy.get('#autor').type('CesarSchool');
    cy.get('#tema').select('Esportes');
    cy.get('input[type="file"]#capa').selectFile('cypress/fixtures/imagem_teste.jpg', { force: true });
    cy.contains('button', 'Criar Notícia').click();
    
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste de Notícia').should('be.visible');
    
    cy.contains('Teste de Notícia').click();

    cy.url().should('include', '/noticia_detalhe/');
    
    cy.get('.comentarios-input')
      .should('be.visible')
      .type('comentário teste.');
    
    cy.get('.noticia-comentarios-form-inline button[type="submit"]').click();
    
    cy.wait(1000);
    cy.contains('Teste de Notícia').should('be.visible');
    
    cy.contains('Teste de Notícia').click();

    
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