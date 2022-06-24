from django.urls import path

from .views import Home, entrar, Homecursos, Detalhescursos

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("cursos/", Homecursos.as_view(), name="homecursos"),
    path("cursos/<int:pk>", Detalhescursos.as_view(), name="detalhescursos"),
    path("login/", entrar, name="login"),
]