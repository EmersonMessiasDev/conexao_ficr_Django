from .models import Curso, Usuario
from .forms import CriarContaForm, FormHomepage
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#! url - view - html
# Pagina_Principal
#? class
class Home(FormView):
    template_name = "home/home.html"
    form_class = FormHomepage
    
    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:homecursos")
        else:
            return super().get(request, *args, **kwargs) #redireciona para a homePage
        
    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('home:login')
        else:
            return reverse('home:criarconta')



class Homecursos(LoginRequiredMixin,ListView):
    template_name = "home/homecursos.html"
    model = Curso
    # object_list -> lista de itens do modelo
    

class Detalhescursos(LoginRequiredMixin, DetailView):
    template_name = "home/detalhescurso.html"
    model = Curso
    # object -> 1 item do nosso modelo
    
    def get(self, request, *args, **kwargs):
        # decobrir qual filme ele ta acessando
        curso = self.get_object()
        # somar 1 nas vizualizações daquele filme
        curso.visualizacao += 1
        #  salvar
        curso.save()
        usuario = request.user
        usuario.cursos_vistos.add(curso)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final
    
    def get_context_data(self, **kwargs):
        context = super(Detalhescursos, self).get_context_data(**kwargs)
        # filtrar tabela de cursos pegando curso cuja categoria é igual a categoria do curso object
        cursos_relacionados = Curso.objects.filter(categoria = self.get_object().categoria)[0:5]
        context["cursos_relacionados"] = cursos_relacionados
        return context

class Pesquisa(LoginRequiredMixin, ListView):
    template_name = "home/pesquisa.html"
    model = Curso
    
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Curso.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin ,UpdateView):
    template_name = "home/editarperfil.html"
    model = Usuario
    fields = ['first_name','last_name', 'email']
    
    def get_sucess_url(self):
        return reverse('home:homecursos')
    
class Criarconta(FormView):
    template_name = "home/criarconta.html"
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('home:login')



# ? Função
# def home(request):
#     return render(request, "home/home.html")

# Pagina de Cursos indicados
# def homecursos(request):
#     context = {}
#     lista_curso = Curso.objects.all()
#     context['lista_curso'] = lista_curso
#     return render(request, "home/homecursos.html", context)