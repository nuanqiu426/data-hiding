from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('login/',views.login_green),
    path('register/',views.reg),
    path('whisper/',views.whis),
    path('answer/',views.ans),
]