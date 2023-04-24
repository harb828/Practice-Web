from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")

# def harv(request):
#     return HttpResponse("Hi Harvey!")

def greet(request, name):
    return HttpResponse(f"Hi, {name.capitalize()}")