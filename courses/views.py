from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(r):
    return HttpResponse('<h1> Welcome to YouTube live Session on CICD</h1>')

def greet_url(r):
    return HttpResponse('<h1> Complete intergration Done</h1>')