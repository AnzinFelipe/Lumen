from django.contrib import admin
from .models import Noticia, Tema
from django.contrib.auth.models import ContentType

admin.site.register(Noticia)
admin.site.register(Tema)



# Register your models here.
