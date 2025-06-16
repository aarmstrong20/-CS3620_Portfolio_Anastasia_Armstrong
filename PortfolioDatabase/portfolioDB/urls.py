from . import views
from django.urls import path


app_name = 'portfolioDB'
urlpatterns = [
    path('', views.Home, name='home'),
    path('portfolio/', views.Portfolios, name='Portfolio'),
    path('portfolio/<int:portfolio_id>/', views.PortfolioDetail, name='portfolio_detail'),
    path('contact/', views.Contact, name='Contact'),
    path('Hobbies/', views.Hobbies, name='Hobbies'),
path('hobby/<int:hobby_id>/', views.HobbyDetail, name='hobby_detail'),
]
