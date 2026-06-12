from django.contrib import admin
from .models import Cliente, Projeto, Skill, Tecnologia


admin.site.register(Projeto)
admin.site.register(Tecnologia)
admin.site.register(Skill)
admin.site.register(Cliente)
