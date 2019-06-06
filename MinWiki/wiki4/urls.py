from django.urls import path

from . import views

urlpatterns = [
    path('', views.wiki4, name='wiki4'),
    path('blocks', views.blocks4, name='bindex4.html'),
    path('zones', views.zones4, name='zindex4.html'),
    path('enemies', views.enemies4, name='eindex4.html'),
    path('items', views.items4, name='iindex4.html'),
    path('weapons', views.weapons4, name='windex4.html'),
    path('mechs', views.mechs4, name='mindex4.html'),
    
]