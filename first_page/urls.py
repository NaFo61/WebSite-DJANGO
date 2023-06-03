from django.urls import path
from .views import *

urlpatterns = [
    path('', first_page, name='Начальная страница'),
]