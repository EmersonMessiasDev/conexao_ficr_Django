from .models import Curso
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

#! url - view - html
# Pagina_Principal
#? class
class Home(TemplateView):
    template_name = "home/home.html"


class Homecursos(ListView):
    template_name = "home/homecursos.html"
    model = Curso
    # object_list -> lista de itens do modelo
    

class Detalhescursos(DetailView):
    template_name = "home/detalhescurso.html"
    model = Curso
    # object -> 1 item do nosso modelo



def entrar(request):
    return render(request,"home/login.html")
    
    




# ? Função
# def home(request):
#     return render(request, "home/home.html")

# Pagina de Cursos indicados
# def homecursos(request):
#     context = {}
#     lista_curso = Curso.objects.all()
#     context['lista_curso'] = lista_curso
#     return render(request, "home/homecursos.html", context)