from django.contrib import admin
from .models import Noticia, Tema, Comentario
from django.contrib.auth.models import ContentType

admin.site.register(Noticia)
admin.site.register(Tema)
admin.site.register(Comentario)



# Register your models here.
