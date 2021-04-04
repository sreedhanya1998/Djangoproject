"""mobiledetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
"""MobileProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path
from .views import mobile_registration,signin,signout,create_mobile,mobile_list,mobile_view,status_Check,sucess,payment,mobile_edit,loginpage,mainlist
urlpatterns = [
path('', lambda request: render(request, "mobile/base.html")),
   path('register',mobile_registration,name="register"),
   path("signin",signin,name="signin"),
   path("signout",signout,name="signout"),
path("create",create_mobile,name="create"),
   path("list",mobile_list,name="list"),
   path("view/<int:id>",mobile_view,name="view"),
   path("status",status_Check,name="status"),
   path('success',sucess,name="sucess"),
   path('pay',payment,name="pay"),
   path("edit/<int:pk>",mobile_edit,name="edit"),
   path("login",loginpage,name="login"),
   path("mainlist",mainlist,name="mainlist")

]
