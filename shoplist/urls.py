from django.urls import path
from .views import *

urlpatterns = [
    path('', shoplist, name='Страница с товарами'),
]