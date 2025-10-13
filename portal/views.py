from django.shortcuts import redirect, render
from portal.forms import NoticiaForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator
from portal.models import Noticia


# Create your views here.

def home(request):
    return render(request, 'portal/home.html')

@has_permission_decorator('pode_publicar')
def criar_noticia(request):
    if request.method == 'GET':
        form = NoticiaForm()
        contexto = {
            'form': form
        }
        return render(request, 'portal/criar_noticia.html', contexto)
    else:
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
def esportes(request):
    noticias = Noticia.objects.all().order_by('-data')

    contexto = {'noticias': noticias}
    return render(request, 'portal/esportes.html', contexto)

def politica(request):
    noticias = Noticia.objects.all().order_by('-data')

    contexto = {'noticias': noticias}
    return render(request, 'portal/politica.html', contexto)

def economia(request):
    noticias = Noticia.objects.all().order_by('-data')

    contexto = {'noticias': noticias}
    return render(request, 'portal/economia.html', contexto)