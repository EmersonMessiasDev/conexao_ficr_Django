from django.contrib import admin
from .models import Curso, Episodio

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "visualizacao", "data_criacao")

class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("curso", "titulo")

# Register your models here.
admin.site.register(Curso, CursoAdmin )

admin.site.register(Episodio, EpisodioAdmin )