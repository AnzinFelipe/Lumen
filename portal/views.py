from django.shortcuts import redirect, render
from portal.forms import NoticiaForm

# Create your views here.

def home(request):
    return render(request, 'portal/home.html')

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