"""
URL configuration for PortfolioDatabase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_view
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', include('portfolioDB.urls')),
    path('register/', accounts_view.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', accounts_view.profile, name='profile'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)