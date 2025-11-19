from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username

class Tema(models.Model):
    tema = models.CharField(max_length = 50)

    def __str__(self):
        return self.tema

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, blank = False)
    subtitulo = models.CharField(max_length=200, blank = False)
    texto = models.TextField(null = True, blank = False)
    autor = models.CharField(max_length=50, blank = False)
    data = models.DateTimeField("Publicado em: ", auto_now_add = True)
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE, related_name='noticias')
    visualizacoes = models.IntegerField(default=0)
    capa = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"
    
class Comentario(models.Model):
    coment_noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE, related_name='comentarios')
    texto = models.TextField(blank = False)
    data = models.DateTimeField("Publicado em: ", auto_now_add = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')

    def __str__(self):
        return f"{self.usuario.username if self.usuario else 'Anônimo'} - {self.coment_noticia.titulo}"

class HistoricoLeitura(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE)
    data = models.DateTimeField("Lido em: ", auto_now_add = True)

    def __str__(self):
        return f"{self.usuario.username} - {self.noticia.titulo}"



