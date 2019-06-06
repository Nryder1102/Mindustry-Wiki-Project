from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def wiki3(request):
    template = loader.get_template('index3.html')
    return HttpResponse(template.render())