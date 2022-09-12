# 引入需要的模块
from django.db import models


# Create your models here.
# 创建用户表

class UsersInfo(models.Model):
    email = models.EmailField(verbose_name="邮箱", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)  # db_index=True创建索引
    password = models.CharField(verbose_name="密码", max_length=32)
