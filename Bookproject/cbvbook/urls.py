"""Bookproject URL Configuration

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
from django.urls import path,include
from django.conf.urls.static import static,settings
from .views import book_list,book_detail,book_create,book_update,book_delete,list_book,detail_book


urlpatterns = [
path('list',book_list.as_view(),name="list"),
    path('view:<int:pk>',book_detail.as_view(),name="view"),
    path('create',book_create.as_view(),name="create"),
path('update/<int:pk>',book_update.as_view(),name="update"),
    path("delete/<int:pk>",book_delete.as_view(),name="delete"),
    path('booklist',list_book.as_view(),name="booklist"),
    path("bookdetail/<int:pk>",detail_book.as_view(),name="bookdetail")


]
