# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. My name is Rachit Poudel. ")

# Create your views here.
