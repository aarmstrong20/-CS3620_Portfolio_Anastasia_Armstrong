from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobby
# Create your views here.
def Home(request):
    return HttpResponse("Hello, world. You're at the home page. To get to portfolio: /portfolio/  hobbies: /Hobbies/ Contact: /contact/")
def Portfolios(request):
    portfolio = Portfolio.objects.all()
    return HttpResponse(portfolio)
def Hobbies(request):
    hobby = Hobby.objects.all()
    return HttpResponse(hobby)
def Contact(request):
    return HttpResponse("My contact info")