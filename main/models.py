from django.db import models

# Create your models here.

class entity(models.Model):
    kor = models.BooleanField()
    usa = models.BooleanField()
    jpn = models.BooleanField()
    hkh = models.BooleanField()
