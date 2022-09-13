from django.urls import path

from users.views import account

urlpatterns = [
    path('register/', account.register, name='register'),
    path('login/', account.login, name='login'),
    path('image/code/', account.image_code, name="image_code")
]



