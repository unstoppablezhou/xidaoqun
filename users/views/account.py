from django.http import JsonResponse
from users.forms import regiseter
from django.shortcuts import render
from users import models


def login(request):
    return render(request, "users/login.html")


def register(request):
    if request.method == 'GET':
        form = regiseter.RegisterModelForm()
        return render(request, "users/register.html", {"form": form})

    form = regiseter.RegisterModelForm(data=request.POST)
    if form.is_valid():
        form.save()  # 等于下面代码，删除数据库中没有的项，如重复密码
        """
        data = form.cleaned_data
        data.pop('confirm_password')
        instance = models.UsersInfo.objects.create(**data)
        """
        return JsonResponse({'status': True, 'data': '/login'})
    # else:print(form.errors)

    return JsonResponse({'status': False, 'error': form.errors})



