from django.shortcuts import render
from .models import Projeto

# Create your views here.
def home(request):
    projetos = Projeto.objects.all()

    return render(request, 'core/pages/home.html',context={
        'projetos': projetos
    })
