from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo}"
    


class Materia(models.Model):
    cabecalho = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto = models.CharField(max_length=50000)


    def __str__(self):
        return f"{self.texto}"
