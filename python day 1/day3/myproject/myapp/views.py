from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, World!")

def goodbye_view(request):
    return HttpResponse("Goodbye, World!")
