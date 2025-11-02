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

Cypress.Commands.add('criarUsuario', () => {
  cy.visit('http://127.0.0.1:8000/registrar/');

  cy.get('#username').should('be.visible');

  cy.get('#username').type('TestandoCypress7');
  cy.get('#email').type('testeCypress7@gmail.com');
  cy.get('#senha').type('12345678');
  cy.get('#senhaconfirmar').type('12345678');

  cy.get('button[type="submit"]').click();
  cy.wait(2000);
  cy.url().should('not.include', '/registrar/');
});

Cypress.Commands.add('fazerLogin', () => {
  cy.visit('http://127.0.0.1:8000/accounts/login/');
  cy.get('#username').type('TestandoCypress7');
  cy.get('#password').type('12345678');
  cy.get('button[type="submit"]').click();

  cy.url().should('not.include', '/accounts/login/');
});

describe('Fluxo do usuário', () => {
  before(() => {
    cy.deleteUsers(); 
  });

  it('deve criar um usuario e fazer login no site', () => {
    cy.criarUsuario();
    cy.fazerLogin();
    cy.contains('Noticias').should('be.visible');
  });
});