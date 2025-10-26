from django.shortcuts import redirect, render
from portal.forms import NoticiaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator
from portal.models import Noticia
from .forms import NoticiaForm
from .models import Noticia, Comentario, Perfil
from django.db import IntegrityError

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

def registrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        senhaconfirmar = request.POST.get('senhaconfirmar')
        email = request.POST.get('email', '')
        erros = []
        if not username:
            erros.append('Nome de usuário é obrigatório')
        elif len(username) < 5:
            erros.append('Nome de usuário deve ter pelo menos 5 caracteres')
        elif User.objects.filter(username=username).exists():
            erros.append('Este nome de usuário já existe')
        if not senha:
            erros.append('Senha é obrigatória')
        elif len(senha) < 8:
            erros.append('Senha deve ter pelo menos 8 caracteres')
        
        if senha != senhaconfirmar:
            erros.append('As senhas não coincidem')
        
        if email and User.objects.filter(email=email).exists():
            erros.append('Este email já está em uso')
        if not erros:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=senha,
                    email=email
                )
                Perfil.objects.create(user=user)
                user = authenticate(request, username=username, password=senha)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    erros.append('Erro ao fazer login')
                    
            except IntegrityError:
                erros.append('Erro ao criar usuário')
        if erros:
            return render(request, 'registration/register.html', {
                'errors': erros,
                'username': username,
                'email': email
            })
    else:
        return render(request, 'registration/register.html')

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
            return render(request, 'login.html', {
                'errors': ['Nome de usuário ou senha incorretos.']
            })
    return render(request, 'registration/login.html')


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
    comentarios = Comentario.objects.filter(coment_noticia = noticia).order_by("-data")
    outras_noticias = Noticia.objects.filter(tema=noticia.tema).exclude(id=noticia.id).order_by('-data')[:3]
    contexto = {
        'noticia' : noticia,
        'comentarios' : comentarios,
        'outras_noticias' : outras_noticias,
    }
    if request.method == 'POST':
        texto = request.POST.get('texto')
        noticia_novo_coment = noticia
        novo_comentario = Comentario(texto = texto, coment_noticia = noticia_novo_coment)
        if not request.user.is_authenticated:
            return redirect('registrar')
        else:
            novo_comentario.save()
            return redirect('home')
    return render(request, 'portal/noticia_detalhe.html', contexto)