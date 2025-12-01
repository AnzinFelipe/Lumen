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
    path('pesquisa/', views.pesquisa_noticia, name='pesquisa-noticia'),
    path('personalizada/', views.busca_personalizada, name='busca_personalizada'),
    path('politica_local/', views.politica_local, name='politica_local'),
    path('politica_global/', views.politica_global, name='politica_global'),
    path('clima_global/', views.clima_global, name='clima_global'),
    path('clima_local/', views.clima_local, name='clima_local'),
    path('saude_bem-estar/', views.saude, name='saude_bem-estar'),
    path('educacao/', views.educacao, name='educacao'),
    path('seguranca/', views.seguranca, name='seguranca'),
    path('cultura/', views.cultura, name='cultura'),
    path('mobilidade/', views.mobilidade, name='mobilidade'),
    path('receita/', views.receita, name='receita'),
    path('climatica/', views.clima, name='clima'),
]
