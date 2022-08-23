from django.shortcuts import render

# 导入forms模块
from django import forms

# 导入users中的models
from users import models

# Create your views here.
from django.http import HttpResponse

# 注册功能

class RegisterModelForm(forms.ModelForm):

    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput)

    code = forms.CharField(label="验证码")
    class Meta:
        model = models.UserInfo
        fields = "__all__"

def register(request):
    form = RegisterModelForm()
    return render(request, "register/register.html", {"form": form})

def login(request):
    return render(request, "login/login.html")

