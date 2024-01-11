from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def main(request):
    return HttpResponse("<h1>Main</h1>")