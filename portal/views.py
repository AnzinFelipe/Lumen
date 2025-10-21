from django.shortcuts import redirect, render
from portal.forms import NoticiaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator
from portal.models import Noticia
from .forms import NoticiaForm
from .models import Noticia


# Create your views here.

def home(request):
    return render(request, 'portal/home.html')


def noticia_list(request):
    template_name = 'portal/noticia-list.html'
    noticias = Noticia.objects.all()
    context = {
        'noticias': noticias
    }
    return render(request, template_name, context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'portal/login.html', {'error': 'Usuário não encontrado ou senha incorreta.'})

    return render(request, 'portal/login.html')


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

def noticia_detalhe(request, id):
    noticia = Noticia.objects.get(pk = id)
    outras_noticias = Noticia.objects.filter(tema=noticia.tema).exclude(id=noticia.id).order_by('-data')[:3]
    contexto = {
        'noticia' : noticia,
        'outras_noticias' : outras_noticias,
    }
    return render(request, 'portal/noticia_detalhe.html', contexto)