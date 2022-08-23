# 引入需要的模块
from django.db import models

# Create your models here.

# 定义用户信息类型
class UserInfo(models.Model):

    userEmail = models.EmailField(verbose_name="邮箱", max_length=32)
    userName = models.CharField(verbose_name="名称", max_length=32)
    passWord = models.CharField(verbose_name="密码", max_length=32)


