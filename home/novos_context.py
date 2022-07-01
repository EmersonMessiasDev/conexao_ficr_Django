from .models import Curso, Usuario
# criar variaveis que vou ter acesso dentro dos HTMLs


def lista_cursos_recentes(request):
    lista_cursos = Curso.objects.all().order_by("data_criacao")[0:8]
    if lista_cursos:
        curso_destaque = lista_cursos[0]
    else:
        curso_destaque = None
    return {"lista_curso_recentes": lista_cursos, "curso_destaque": curso_destaque}

def lista_cursos_em_alta(request):
    lista_cursos = Curso.objects.all().order_by("-visualizacao")[0:8]
    return {"lista_cursos_em_alta": lista_cursos}

def front_end(request):
    lista_cursos = Curso.objects.filter(categoria ='FRONT-END')[0:8]
    return {"front_end": lista_cursos}

def comece_aqui(request):
    lista_cursos = Curso.objects.filter(categoria = 'COMECE_AQUI')[0:8]
    return {'comece_aqui':lista_cursos}