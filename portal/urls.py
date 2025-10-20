from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('criar_noticia/', views.criar_noticia, name='criar_noticia'),
    path('login/', views.Login, name='login'),
    path('esportes/', views.esportes, name='esportes'),
    path('economia/', views.economia, name='economia'),
    path('politica/', views.politica, name='politica'),
    path('noticia_detalhe/<int:id>', views.noticia_detalhe, name='noticia_detalhe'),
    path('account/login/', views.Login, name='account_login'),
]
