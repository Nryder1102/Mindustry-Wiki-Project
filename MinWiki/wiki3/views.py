from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('wiki3/index3.html')
    return HttpResponse(template.render())