from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse("Hello")

# Using the index.html in templates/hi
def index(request):
    return render(request, "hi/index.html")

# def harv(request):
#     return HttpResponse("Hi Harvey!")

def greet(request, name):
    return HttpResponse(f"Hi, {name.capitalize()}")