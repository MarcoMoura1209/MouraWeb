from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'tecnologia'
        verbose_name_plural = 'Tecnologias'

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    link_github = models.URLField()
    imagem = models.ImageField(upload_to='projetos/')
    tecnologias = models.ManyToManyField(Tecnologia)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo


class Skill(models.Model):
    nome = models.CharField(max_length=50)
    porcentagem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    mensagem = models.TextField(max_length=1500, blank=False, null=False)

    class Meta: 
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def clean(self):
        if len(self.mensagem) > 1500:
            raise ValidationError({
                'mensagem': 'A mensagem deve ter no máximo 1500 caracteres.'
            })

    def __str__(self):
        return self.nome
