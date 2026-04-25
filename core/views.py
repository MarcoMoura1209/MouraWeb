from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from .models import Projeto, Skill
from .forms import Form


@ratelimit(key='ip', rate='5/h', method='POST', block=True)
def home(request):
    projetos = Projeto.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = Form()

    return render(request, 'core/pages/home.html', context={
        'projetos': projetos,
        'skills': skills,
        'form': form,
    },)
