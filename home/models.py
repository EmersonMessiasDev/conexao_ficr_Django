from django.utils import timezone
from distutils.command.upload import upload
from django.db import models

#? criando categoria cursos
#? armazenar no banco - mostrar ao usuario 
LISTA_CATEGORIAS =(
    ("FRONT-END","FRONT-END"),
    ("BACK-END","BACK_END"),
    ("GITHUB","GIT - GITHUB"),
    ("BANCO_DE_DADOS","BANCO DE DADOS"),
    ("OUTROS", "OUTROS"),
    ("INGLES", "INGLÊS"),
) 

#criar cursos
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_cursos')
    descicao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=25, choices=LISTA_CATEGORIAS)
    vizualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
