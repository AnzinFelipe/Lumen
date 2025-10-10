from django.db import models

class Tema(models.Model):
    tema = models.CharField(max_length = 50)

    def __str__(self):
        return self.tema

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, blank = False)
    subtitulo = models.CharField(max_length=200, blank = False)
    texto = models.TextField(blank = False)
    autor = models.CharField(max_length=50, blank = False)
    data = models.DateTimeField("Publicado em: ", auto_now_add = True)
    tema = models.ForeignKey(Tema, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"
    