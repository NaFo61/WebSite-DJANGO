from django.db import models

class Developers(models.Model):
    user = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, default='Не указан')