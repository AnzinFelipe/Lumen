from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('criar_noticia', views.criar_noticia, name = 'criar_noticia'),
]
