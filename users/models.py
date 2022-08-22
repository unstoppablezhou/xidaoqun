# 引入需要的模块
from django.db import models

# Create your models here.

# 定义用户类型
class Users(models.Model):

    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)


