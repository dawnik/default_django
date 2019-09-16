from django.db import models
from django.contrib.auth.models import User

class Termin(models.Model):
    data = models. DateTimeField(auto_now_add=True)
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=9)
    telefon = models.CharField(max_length=9)
    kwota = models.CharField(max_length=9)