from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'portfolioDB/home.html')
def Portfolio(request):
    return render(request, 'portfolioDB/portfolio.html')
def Hobbies(request):
    return render(request, 'portfolioDB/hobbies.html')
def ContactU(request):
    return render(request, 'portfolioDB/contact.html')