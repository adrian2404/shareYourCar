from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo_view(request):
    return HttpResponse('<h1> Hello world </h1>')