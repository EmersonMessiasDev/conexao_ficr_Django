from django.urls import path

from .views import Home, entrar, Homecursos

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("cursos/", Homecursos.as_view(), name="homecursos"),
    path("login/", entrar, name="login"),
]