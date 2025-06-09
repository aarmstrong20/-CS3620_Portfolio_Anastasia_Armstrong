from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("Hello, world. You're at the polls page.")
def Portfolio(request):
    return render(request, 'portfolioDB/portfolio.html')
def Hobbies(request):
    return render(request, 'portfolioDB/hobbies.html')
def Contact(request):
    return render(request, 'portfolioDB/contact.html')