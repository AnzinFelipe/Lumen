from rolepermissions.roles import AbstractUserRole

class Editor(AbstractUserRole):
    available_permissions = {
        'pode_publicar': True,
        'pode_editar': True,
        'pode_deletar': True,
        'pode_visualizar': True,
    }   

class Leitor(AbstractUserRole):
    available_permissions = {
        'pode_visualizar': True,
    }

