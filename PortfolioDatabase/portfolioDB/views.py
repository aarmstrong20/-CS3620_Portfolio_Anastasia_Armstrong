from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobby
from django.template import loader

# Create your views here.
def Home(request):
   template = loader.get_template('portfolioDB/home.html')
   return render(request, 'portfolioDB/home.html')

def Portfolios(request):
    context = {
        'portfolio': Portfolio.objects.all(),
    }
    return render(request, 'portfolioDB/portfolio.html', context)

def PortfolioDetail(request, portfolio_id):
   context = {
       'portfolio': Portfolio.objects.get(pk=portfolio_id),
   }
   return render(request, 'portfolioDB/portfolio_detail.html', context)

def Hobbies(request):
    context = {
        'hobbies': Hobby.objects.all(),
    }
    return render(request, 'portfolioDB/hobbies.html', context)


def HobbyDetail(request, hobby_id):
    context ={
        'hobby': Hobby.objects.get(pk=hobby_id),
    }
    return render(request, 'portfolioDB/hobby_detail.html', context)
def Contact(request):
    return render(request, 'portfolioDB/contact.html')