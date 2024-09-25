from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def service(request):
    return HttpResponse("este es un servicio")

def blog(request):
    return HttpResponse("este es un blog")
# Create your views here.
