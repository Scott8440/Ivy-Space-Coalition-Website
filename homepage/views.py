from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def register(request):
    return render(request, 'homepage/register.html')
