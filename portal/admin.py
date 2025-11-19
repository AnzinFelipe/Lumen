from django.contrib import admin
from .models import Perfil, Tema, Noticia, Comentario, HistoricoLeitura

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data', 'tema', 'visualizacoes')
    list_filter = ('tema', 'data')
    search_fields = ('titulo', 'subtitulo', 'texto', 'autor')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('coment_noticia', 'usuario', 'data')
    search_fields = ('texto', 'usuario__username', 'coment_noticia__titulo')

admin.site.register(Perfil)
admin.site.register(Tema)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(HistoricoLeitura)
