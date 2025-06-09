from django.db import models

# Create your models here.
class Portfolio(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=60)
    portfolio_desc = models.CharField(max_length=500)

class Hobby(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=60)
    hobby_desc = models.CharField(max_length=500)