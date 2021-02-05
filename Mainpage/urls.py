from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('success/',views.login_success),
    path('knowme/',views.You_know_me)
]