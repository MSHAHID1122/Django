from django.contrib import admin
from django.urls import path
from finance.views import RegisterView,Dashboard,TranscationView
urlpatterns = [
    # path('home/',home,name="home"),
    # path('myhome/',Home.as_view(),name="myhome")

    path("register",RegisterView.as_view(),name="register"),
    path('',Dashboard.as_view(),name='dashboard'),
    path('transcation',TranscationView.as_view(),name='transcation')
]
