
from django.shortcuts import render



def home(request):
    return render(request, "home/home.html")

def entrar(request):
    return render(request,"home/login.html")
    
    
