from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def service(request):
    return render(request, 'myapp/service.html')

def blog(request):
    return render(request, 'myapp/blog.html')
def prtafolio(request):
    return render(request, 'myapp/portafolio.html')
# Create your views here.
