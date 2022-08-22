from django.contrib import admin

# Register your models here.
#引入模块
from .models import Users

admin.site.register(Users)