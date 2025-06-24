from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolioDB'
urlpatterns = [
    path('', views.Home, name='home'),
    path('Home', views.Home, name='home'),
    path('portfolio/', views.Portfolios, name='Portfolio'),
    path('portfolio/<int:portfolio_id>/', views.PortfolioDetail, name='portfolio_detail'),
    path('contact/', views.Contact, name='Contact'),
    path('Hobbies/', views.Hobbies, name='Hobbies'),
path('hobby/<int:hobby_id>/', views.HobbyDetail, name='hobby_detail'),
    path('contact/message/', views.ContactMessage, name='ContactMessage'),
    path('portfolio/add', views.PortfolioAdd, name='PortfolioAdd'),
    path('portfolio/edit/<int:portfolio_id>/', views.PortfolioEdit, name='PortfolioEdit'),
    path('portfolio/delete/<int:portfolio_id>/', views.PortfolioDelete, name='PortfolioDelete'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)