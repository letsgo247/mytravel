from django.db import models

# Create your models here.

class Entity(models.Model):
    kor = models.BooleanField(default=False)
    usa = models.BooleanField(default=False)
    jpn = models.BooleanField(default=False)
    hkg = models.BooleanField(default=False)
