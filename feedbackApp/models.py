from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length= 200) 

class Grupo(models.Model):
    nomeDoGrupo = models.CharField(max_length= 200)  
    alunos = models.ManyToManyField(Aluno, related_name='grupos')


#alo perdi o chat
#n lembro onde fica
