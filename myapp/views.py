from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h4>This is home page TESTING</h4>")

def about(request):
    return HttpResponse("<h1>This is about page TESTING</h1>")