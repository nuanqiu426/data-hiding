from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    # path('',views.new_encode),
    path('',views.encode_processing)
]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)