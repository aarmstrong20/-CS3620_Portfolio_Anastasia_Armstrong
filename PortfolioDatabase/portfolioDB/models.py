from django.db import models

# Create your models here.
class Portfolio(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=60)
    portfolio_desc = models.CharField(max_length=500)
    image = models.CharField(max_length=600, default='https://cdn-icons-png.flaticon.com/512/135/135161.png')
class Hobby(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=60)
    hobby_desc = models.CharField(max_length=500)
    image = models.CharField(max_length=600, default='https://cdn-icons-png.flaticon.com/512/135/135161.png')


class Contact(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
