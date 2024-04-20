from django.db import models

class Aluno(models.Model):
    nome = models.CharField()  

class Grupo(models.Model):
    nomeDoGrupo = models.CharField()  
    alunos = models.ManyToManyField(Aluno, related_name='grupos')


