from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.nlp_test),
    path('s/',views.nlp_final)

]