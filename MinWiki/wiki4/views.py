
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def wiki4(request):
    template = loader.get_template('index4.html')
    return HttpResponse(template.render())

def blocks4(request):
    template = loader.get_template('bindex4.html')
    return HttpResponse(template.render())

def zones4(request):
    template = loader.get_template('zindex4.html')
    return HttpResponse(template.render())

def enemies4(request):
    template = loader.get_template('eindex4.html')
    return HttpResponse(template.render())

def items4(request):
    template = loader.get_template('iindex4.html')
    return HttpResponse(template.render())

def weapons4(request):
    template = loader.get_template('windex4.html')
    return HttpResponse(template.render())

def mechs4(request):
    template = loader.get_template('mindex4.html')
    return HttpResponse(template.render())

#Items things

def copper(request):
    template = loader.get_template('copper.html')
    return HttpResponse(template.render())

def coal(request):
    template = loader.get_template('coal.html')
    return HttpResponse(template.render())

def bcompound(request):
    template = loader.get_template('blast compound.html')
    return HttpResponse(template.render())

def graphite(request):
    template = loader.get_template('graphite.html')
    return HttpResponse(template.render())

def lead(request):
    template = loader.get_template('lead.html')
    return HttpResponse(template.render())

def mglass(request):
    template = loader.get_template('metaglass.html')
    return HttpResponse(template.render())

def pfab(request):
    template = loader.get_template('phase fabric.html')
    return HttpResponse(template.render())

def plastanium(request):
    template = loader.get_template('plastanium.html')
    return HttpResponse(template.render())

def pyratite(request):
    template = loader.get_template('pyratite.html')
    return HttpResponse(template.render())

def sand(request):
    template = loader.get_template('sand.html')
    return HttpResponse(template.render())

def scrap(request):
    template = loader.get_template('scrap.html')
    return HttpResponse(template.render())

def silicon(request):
    template = loader.get_template('silicon.html')
    return HttpResponse(template.render())

def spod(request):
    template = loader.get_template('spore pod.html')
    return HttpResponse(template.render())

def salloy(request):
    template = loader.get_template('surge alloy.html')
    return HttpResponse(template.render())

def thorium(request):
    template = loader.get_template('thorium.html')
    return HttpResponse(template.render())

def titanium(request):
    template = loader.get_template('titanium.html')
    return HttpResponse(template.render())


#
