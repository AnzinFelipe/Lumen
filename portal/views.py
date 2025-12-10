from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test # ADICIONADO
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission_decorator
from portal.models import Noticia
from .models import Noticia, Comentario, Perfil, HistoricoLeitura
from django.db import IntegrityError
from portal.models import Tema
# Create your views here.

def home(request): # ADADAPITADO
    # Últimas notícias por data
    ultimas_noticias = Noticia.objects.all().order_by('-data')

    # Todas as demais seções por visualizações
    noticias_relevantes = Noticia.objects.all().order_by('-visualizacoes', '-data')
    temas_pernambuco = Tema.objects.filter(tema__in=["Climática Local", "Política Local"])
    pernambuco_noticias = Noticia.objects.filter(tema__in=temas_pernambuco).order_by('-visualizacoes', '-data')
    videos_tv_jornal = Noticia.objects.all().order_by('-visualizacoes', '-data')
    tema_esportes = Tema.objects.filter(tema="Esportes").first()
    if tema_esportes:
        blog_torcedor = Noticia.objects.filter(tema=tema_esportes).order_by('-visualizacoes', '-data')
    else:
        blog_torcedor = Noticia.objects.none()
    social_1 = Noticia.objects.all().order_by('-visualizacoes', '-data')
    tema_receita = Tema.objects.filter(tema="Receita").first()
    if tema_receita:
        receita_da_boa = Noticia.objects.filter(tema=tema_receita).order_by('-visualizacoes', '-data')
    else:
        receita_da_boa = Noticia.objects.none()

    noticias_populares = get_noticias_populares()
    mais_lidas = Noticia.objects.all().order_by('-visualizacoes', '-data')
    
    # Social 1 - Filtros por tema
    tema_cultura = Tema.objects.filter(tema="Cultura").first()
    if tema_cultura:
        social_signos = Noticia.objects.filter(tema=tema_cultura).order_by('-visualizacoes', '-data')
    else:
        social_signos = Noticia.objects.none()
    
    tema_entretenimento = Tema.objects.filter(tema="Entretenimento").first()
    if tema_entretenimento:
        social_series = Noticia.objects.filter(tema=tema_entretenimento).order_by('-visualizacoes', '-data')
        social_agnews = Noticia.objects.filter(tema=tema_entretenimento).order_by('-visualizacoes', '-data')
    else:
        social_series = Noticia.objects.none()
        social_agnews = Noticia.objects.none()

    return render(request, 'portal/home.html', {
        'noticias_relevantes': noticias_relevantes,
        'noticias_populares': noticias_populares,
        'ultimas_noticias': ultimas_noticias,
        'pernambuco_noticias': pernambuco_noticias,
        'videos_tv_jornal': videos_tv_jornal,
        'blog_torcedor': blog_torcedor,
        'social_1': social_1,
        'receita_da_boa': receita_da_boa,
        'mais_lidas': mais_lidas,
        'social_signos': social_signos,
        'social_series': social_series,
        'social_agnews': social_agnews,
    })




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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {
                'errors': ['Nome de usuário ou senha incorretos.']
            })
    return render(request, 'registration/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


def criar_noticia(request):
    """
    View para criação de notícias.
    - Acessível apenas para usuários logados e marcados como staff.
    - Salva título, subtítulo, texto, autor, tema, capa, legenda e áudio.
    """
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        autor = request.POST.get('autor')
        tema_id = request.POST.get('tema')

        capa = request.FILES.get('capa')
        audio = request.FILES.get('audio')      # ADICIONADO
        legenda = request.POST.get('legenda')   # ADICIONADO

        erro = None  # ADICIONADO

        
        if not all([titulo, subtitulo, texto, autor, tema_id]):
            erro = "Todos os campos marcados como obrigatórios precisam ser preenchidos."
        elif len(titulo) > 100:
            erro = "O título deve ter no máximo 100 caracteres."
        elif len(subtitulo) > 200:
            erro = "O subtítulo deve ter no máximo 200 caracteres."
        elif len(autor) > 50:
            erro = "O nome do autor deve ter no máximo 50 caracteres."

        if not erro:  # ADICIONADO
            try:
                tema = Tema.objects.get(id=tema_id)

                Noticia.objects.create(
                    titulo=titulo,
                    subtitulo=subtitulo,
                    texto=texto,
                    autor=autor,
                    tema=tema,
                    capa=capa,
                    legenda=legenda,
                    audio=audio
                )
                
                return redirect('home')
            
            except Tema.DoesNotExist:
                erro = "Tema selecionado é inválido!"
 
        return render(
            request,
            'portal/criar_noticia.html',
            {
                'todas_temas': Tema.objects.all(),
                'erro': erro
            }
        )

    
    return render(
        request,
        'portal/criar_noticia.html',
        {
            'todas_temas': Tema.objects.all()
        }
    )

    
def esportes(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/esportes.html', contexto)

def politica(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/politica.html', contexto)

def clima(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/climatica.html', contexto)

def economia(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/economia.html', contexto)

def entretenimento(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/entretenimento.html', contexto)

def tecnologia(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/tecnologia.html', contexto)

def get_noticias_populares():
    return Noticia.objects.order_by('-visualizacoes')[:3]

def politica_local(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/politica_local.html', contexto)

def cultura(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/cultura.html', contexto)

def clima_global(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/climatica_global.html', contexto)

def clima_local(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/climatica_local.html', contexto)

def seguranca(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/seguranca.html', contexto)

def mobilidade(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/mobilidade.html', contexto)

def receita(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/receita.html', contexto)

def saude(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/saude_bem-estar.html', contexto)

def educacao(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/educacao.html', contexto)

def politica_global(request):
    noticias = Noticia.objects.all().order_by('-data')
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticias': noticias,
        'noticias_populares': noticias_populares
    }
    return render(request, 'portal/politica_global.html', contexto)

def noticia_detalhe(request, id):
    noticia = Noticia.objects.get(pk = id)
    noticia.visualizacoes += 1
    noticia.save()
    try:
        if request.user.is_authenticated:
            HistoricoLeitura.objects.create(usuario = request.user,noticia = noticia,tema = noticia.tema)
    except:
        pass
    hist = request.session.get('hist_temas', [])
    hist.insert(0, noticia.tema_id)
    request.session['hist_temas'] = hist[:10]
    request.session.modified = True
    comentarios = Comentario.objects.filter(coment_noticia = noticia).order_by("-data")
    outras_noticias = Noticia.objects.filter(tema=noticia.tema).exclude(id=noticia.id).order_by('-data')[:3]
    noticias_populares = get_noticias_populares()
    contexto = {
        'noticia' : noticia,
        'comentarios' : comentarios,
        'outras_noticias' : outras_noticias,
        'noticias_populares': noticias_populares
    }
    if request.method == 'POST':
        texto = request.POST.get('texto')
        noticia_novo_coment = noticia
        novo_comentario = Comentario(texto = texto, coment_noticia = noticia_novo_coment)
        if not request.user.is_authenticated:
            return redirect('registrar')
        else:
            novo_comentario.usuario = request.user
            novo_comentario.save()
            return redirect('home')
    return render(request, 'portal/noticia_detalhe.html', contexto)

def pesquisa_noticia(request):
    if request.method=='POST':
        objeto = request.POST['objeto']
        noticia = Noticia.objects.filter(titulo__contains=objeto)
        return render(request,'portal/pesquisa.html', {'objeto': objeto, 'noticia': noticia})
    else:
        return render(request,'pesquisa.html')
    
def preferencias_por_tema(request, max_itens = 3):
    if request.user.is_authenticated:
        leituras = list(HistoricoLeitura.objects.filter(usuario = request.user).order_by('-data').values_list('tema_id', flat = True)[:100])
    else: 
        leituras = list(request.session.get('hist_temas', []))

    if not leituras:
        return[]
    score = {}
    peso = 1.0
    for tema_id in leituras:
        score[tema_id] = score.get(tema_id, 0) + peso
        peso *= 0.95
    
    tema_ids = [t for t, _ in sorted(score.items(), key = lambda x: x[1], reverse = True)]
    return tema_ids[:max_itens]

def busca_personalizada(request):
    preferidos = preferencias_por_tema(request, max_itens = 3)
    exclude_id = request.GET.get('exclude')

    noticias = Noticia.objects.none()
    if preferidos:
        qs = Noticia.objects.filter(tema_id__in = preferidos)
        if exclude_id:
            qs = qs.exclude(id = exclude_id)
        noticias = qs.order_by('-visualizacoes', '-data', '-id')

    contexto = {
        'noticias': noticias,
        'temas_preferidos': Tema.objects.filter(id__in = preferidos),
        'noticias_populares': get_noticias_populares()
    }
    return render(request, 'portal/busca_personalizada.html', contexto)