"""uniPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
app_name = "mainApp"
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('matches', views.matches, name='matches'),
    path('Roll', views.Roll, name='Roll'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('Download/Guid/FileGuid/<str:url>', views.downloadG, name='downloadG'),
]
