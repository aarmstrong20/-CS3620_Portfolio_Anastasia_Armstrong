from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobby
from django.template import loader

# Create your views here.
def Home(request):
   template = loader.get_template('portfolioDB/home.html')
   context = {
       'portfolio': Portfolio.objects.all(),
   }
   return render(request, 'portfolioDB/home.html')

def Portfolios(request):
    portfolio = Portfolio.objects.all()
    return HttpResponse(portfolio)
def Hobbies(request):
    hobby = Hobby.objects.all()
    return HttpResponse(hobby)
def Contact(request):
    return HttpResponse("My contact info")