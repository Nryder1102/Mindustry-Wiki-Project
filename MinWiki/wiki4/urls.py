from django.urls import path

from . import views

urlpatterns = [

    #Index paths
    path('', views.wiki4, name='wiki4'),
    path('blocks', views.blocks4, name='bindex4.html'),
    path('zones', views.zones4, name='zindex4.html'),
    path('enemies', views.enemies4, name='eindex4.html'),
    path('items', views.items4, name='iindex4.html'),
    path('weapons', views.weapons4, name='windex4.html'),
    path('mechs', views.mechs4, name='mindex4.html'),

    #Item paths
    path('items/copper', views.copper, name='copper.html'),
    path('items/coal', views.coal, name='coal.html'),
    path('items/blast compound', views.bcompound, name='blast compound.html'),
    path('items/graphite', views.graphite, name='graphite.html'),
    path('items/lead', views.lead, name='lead.html'),
    path('items/metaglass', views.mglass, name='metaglass.html'),
    path('items/phase fabric', views.pfab, name='phase fabric.html'),
    path('items/plastanium', views.plastanium, name='plastanium.html'),
    path('items/pyratite', views.pyratite, name='pyratite.html'),
    path('items/sand', views.sand, name='sand.html'),
    path('items/scrap', views.scrap, name='scrap.html'),
    path('items/silicon', views.silicon, name='silicon.html'),
    path('items/spore pod', views.spod, name='spore pod.html'),
    path('items/surge alloy', views.salloy, name='surge alloy.html'),
    path('items/thorium', views.thorium, name='thorium.html'),
    path('items/titanium', views.titanium, name='titanium.html'),


]