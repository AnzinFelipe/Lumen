from django.urls import path
from . import views
#from .views import HomeView

urlpatterns = [
    path('', views.noticia_list, name='home'),
    path('criar_noticia/', views.criar_noticia, name='criar_noticia'),
    path('accounts/login/', views.Login, name='login'),
    path('esportes/', views.esportes, name='esportes'),
    path('economia/', views.economia, name='economia'),
    path('politica/', views.politica, name='politica'),
    path('noticia_detalhe/<int:id>', views.noticia_detalhe, name='noticia_detalhe'),
    path('registrar/', views.registrar, name='registrar'),
]
