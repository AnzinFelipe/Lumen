Cypress.Commands.add('deleteUsers', () => {
  cy.exec('python delete_users.py', { 
    failOnNonZeroExit: false,
    timeout: 15000 
  }).then((result) => {
    cy.log('Exit code:', result.code);
    if (result.stdout) {
      cy.log('Cleanup result:', result.stdout);
    }
    if (result.stderr) {
      cy.log('Cleanup stderr:', result.stderr);
    }
  });
});

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
    
    cy.visit('http://127.0.0.1:8000/esportes/');
    cy.contains('Teste de Notícia').should('be.visible');
});

  it('deve criar notícia e checar se ela existe na url do tema', () => {
    cy.fazerLogin();
    cy.postarTema();
    
  });
