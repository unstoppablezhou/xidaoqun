from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#注册功能
def register(request):
    return render(request, "register/register.html")

def login(request):
    return render(request, "login/login.html")