
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