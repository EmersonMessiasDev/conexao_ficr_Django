from django.contrib import admin
from .models import Curso, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#? adicionando campos no ADMIN
# ================================================================= #
campos = list(UserAdmin.fieldsets)
campos.append(
("Histórico", {'fields': ('cursos_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)
# ================================================================= #

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "visualizacao", "data_criacao")

class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("curso", "titulo")


# Register your models here.
admin.site.register(Curso, CursoAdmin )

admin.site.register(Episodio, EpisodioAdmin )

admin.site.register(Usuario, UserAdmin)

