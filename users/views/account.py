from users import models
from django.http import JsonResponse, HttpResponse
from users.forms import regiseter_form
from users.forms import login_form
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'GET':
        form = login_form.LoginForm(request)
        return render(request, "users/login.html", {'form': form})
    form = login_form.LoginForm(request, data=request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user_object = models.UsersInfo.objects.filter(email=email, password=password).first()

        if user_object:
            # 用户名密码正确
            print("成功")
            return redirect('index')
        form.add_error('email', '邮箱或密码错误')
    return render(request, "users/login.html", {'form': form})


def register(request):
    if request.method == 'GET':
        form = regiseter_form.RegisterModelForm()
        return render(request, "users/register.html", {"form": form})

    form = regiseter_form.RegisterModelForm(data=request.POST)
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


def image_code(request):
    """ 生产图片"""
    from utils.image_code import check_code
    from io import BytesIO

    image_object, code = check_code()

    # 下面两行代码是把生产的随机码放到session，并设置它的时限为60s
    request.session['image_code'] = code
    request.session.set_expiry(60)

    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())
