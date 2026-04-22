from django.db import models

# Create your models here.

class Tecnologias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'tecnologia'
        verbose_name_plural = 'Tecnologias'

class Projeto(models.Model):
    titulo = models.TextField()
    descricao = models.CharField(max_length=165)
    link_github = models.URLField()
    imagem = models.ImageField(upload_to='projetos/')
    tecnologias = models.ManyToManyField(Tecnologias)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo
