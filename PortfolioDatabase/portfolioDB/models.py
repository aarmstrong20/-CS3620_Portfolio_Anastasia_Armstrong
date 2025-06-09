from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=60)
    portfolio_desc = models.CharField(max_length=500)

class Hobbies(models.Model):
    name = models.CharField(max_length=60)
    Hobbies_desc = models.CharField(max_length=500)