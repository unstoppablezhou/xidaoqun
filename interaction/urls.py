from django.urls import path
from interaction.views import content

urlpatterns = [
   path('index/', content.index, name='index')

]