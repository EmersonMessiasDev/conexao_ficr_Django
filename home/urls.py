from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from .views import Home, Homecursos, Detalhescursos, Pesquisa, Paginaperfil, Criarconta


app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("cursos/", Homecursos.as_view(), name="homecursos"),
    path("cursos/<int:pk>", Detalhescursos.as_view(), name="detalhescursos"),
    path("pesquisa/", Pesquisa.as_view(), name="pesquisa"),
    path("login/", auth_view.LoginView.as_view(template_name='home/login.html'), name='login'),
    path("logout/", auth_view.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path("editarperfil/<int:pk>", Paginaperfil.as_view(), name="editarperfil"),
    path( "criarconta/", Criarconta.as_view(), name="criarconta"),
    path("mudarsenha/", auth_view.PasswordChangeView.as_view(template_name='home/editarperfil.html',
                                                            success_url=reverse_lazy('home:homecursos')), name='mudarsenha'),
]