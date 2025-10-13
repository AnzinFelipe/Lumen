from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('criar_noticia', views.criar_noticia, name = 'criar_noticia'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('esportes/', views.esportes, name = 'esportes'),
    path('economia/', views.economia, name = 'economia'),
    path('politica/', views.politica, name = 'politica'),
    path('noticia_detalhe/<int:id>', views.noticia_detalhe, name = 'noticia_detalhe'),
]
