from . import views
from django.urls import path

app_name = 'Portfolio'
urlpatterns = [
    path('', views.Home, name='home'),
    path('portfolio/', views.Portfolios, name='Portfolio'),
    path('contact/', views.Contact, name='Contact'),
    path('Hobbies/', views.Hobbies, name='Hobbies'),
]
