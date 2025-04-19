from django.contrib import admin
from django.urls import path
from finance.views import home,Home
urlpatterns = [
    path('home/',home,name="home"),
    path('myhome/',Home.as_view(),name="myhome")
]
