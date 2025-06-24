from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobby
from .forms import PortfolioForm
from .forms import ContactForm
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

def PortfolioAdd(request):
    form = PortfolioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolioDB:Portfolio')
    return render(request, 'portfolioDB/portfolio_form.html', {'form': form})


def ContactMessage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Contact from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['tazele@gmail.com'],
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('portfolioDB:Contact')
    else:
        form = ContactForm()
    return render(request, 'portfolioDB/contact_form.html', {'form': form})


def PortfolioEdit(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(request.POST or None, request.FILES or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('portfolioDB:Portfolio')
    return render(request, 'portfolioDB/portfolio_form.html', {'form': form, 'portfolio': portfolio})

def PortfolioDelete(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolioDB:Portfolio')
    return render(request, 'portfolioDB/portfolio_delete.html', {'portfolio': portfolio})

