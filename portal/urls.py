from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar_noticia/', views.criar_noticia, name='criar_noticia'),
    path('accounts/login/', views.Login, name='login'),
    path('esportes/', views.esportes, name='esportes'),
    path('economia/', views.economia, name='economia'),
    path('politica/', views.politica, name='politica'),
    path('entretenimento/', views.entretenimento, name='entretenimento'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('noticia_detalhe/<int:id>', views.noticia_detalhe, name='noticia_detalhe'),
    path('registrar/', views.registrar, name='registrar'),
    path('pesquisa/', views.pesquisa_noticia, name='pesquisa-noticia')
]
