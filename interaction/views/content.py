
from django.shortcuts import render
from django.http import HttpResponse

from interaction import models


# Create your views here.

def index(request):

    # 去数据库中获取所有的列表
    # queryset列表，[对象，对象，对象] 封装一行数据
    queryset = models.InteractionInfo.objects.all()

    return render(request, 'interaction/index.html', {'queryset': queryset})
