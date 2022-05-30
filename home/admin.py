from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "vizualizacao", "data_criacao")

# Register your models here.
admin.site.register(Curso, CursoAdmin )