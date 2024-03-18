"""
URL configuration for RSM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from realestate import views as r_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',r_view.buy, name= 'buy'),
    path('rent/' ,r_view.rent, name='rent'),
    path('buyhome1/' ,r_view.buyhome1, name='buyhome1'),
    path('buyhome2/' ,r_view.buyhome2, name='buyhome2'),
    path('renthome1/' ,r_view.renthome1, name='renthome1'),
    path('renthome2/' ,r_view.renthome2, name='renthome2'),
    path('confirm/' ,r_view.confirm, name='confirm'),


]
