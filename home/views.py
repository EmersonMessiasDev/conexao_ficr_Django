from .models import Curso
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

#! url - view - html
# Pagina_Principal
#? class
class Home(TemplateView):
    template_name = "home/home.html"

class Homecursos(ListView):
    template_name = "home/homecursos.html"
    model = Curso
    

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