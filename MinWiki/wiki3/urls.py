from django.urls import path

from . import views

urlpatterns = [
    path('', views.wiki3, name='wiki3'),
]