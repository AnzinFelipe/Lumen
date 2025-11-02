Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('Cesar');
  cy.get('#password').type('123');
  cy.get('button[type="submit"]').click();

  cy.url().should('not.include', '/accounts/login/');
});

Cypress.Commands.add('postarDuasNoticiaseIrNoLeiaMais', () => {
    cy.visit('http://127.0.0.1:8000/criar_noticia/');
    
    cy.get('#id_titulo').type('Teste de Notícia');
    cy.get('#id_subtitulo').type('Subtítulo do Teste de Notícia');
    cy.get('#id_texto').type('Texto do Teste de Notícia');
    cy.get('#id_autor').type('CesarSchool');
    cy.get('#id_tema').select('Esportes');
    
    cy.contains('button', 'Criar Notícia').click();
    
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste de Notícia').should('be.visible');
    
    cy.visit('http://127.0.0.1:8000/criar_noticia/');
    
    cy.get('#id_titulo').type('Teste para o Leia Mais');
    cy.get('#id_subtitulo').type('Subtítulo do Teste de Leia Mais');
    cy.get('#id_texto').type('Texto do Teste de Leia Mais');
    cy.get('#id_autor').type('CesarSchool');
    cy.get('#id_tema').select('Esportes');
    
    cy.contains('button', 'Criar Notícia').click();

    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste para o Leia Mais').should('be.visible');

    cy.visit('http://127.0.0.1:8000/esportes/');
    cy.contains('Teste de Notícia').should('be.visible');
    cy.contains('Teste de Notícia').click();

    cy.contains('Teste para o Leia Mais').should('be.visible');
});

  it('deve criar duas notícias e checar se uma aparece no Leia Mais da outra', () => {
    cy.fazerLogin();
    cy.postarDuasNoticiaseIrNoLeiaMais();
    
  });