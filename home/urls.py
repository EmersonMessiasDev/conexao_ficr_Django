from django.urls import path

from .views import home, entrar

urlpatterns = [
    path('', home, name="home"),
    path("login/", entrar, name="login"),
]