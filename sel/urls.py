from django.conf.urls import url,patterns, include
from django.contrib import admin
from sel import views

urlpatterns = [
    url(r'^$',views.archive), 
]
