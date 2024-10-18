from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'greet/home.html')

def page_two(request):
    return render(request, 'greet/page_two.html')

def page_three(request):
    return render(request, 'greet/page_three.html')