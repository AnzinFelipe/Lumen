from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('criar_noticia', views.criar_noticia, name = 'criar_noticia'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
]
