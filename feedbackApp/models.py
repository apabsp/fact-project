from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=200) 

class Grupo(models.Model):
    nome = models.CharField(max_length=200)  
    alunos = models.ManyToManyField(Aluno, related_name='grupos')
    professor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
