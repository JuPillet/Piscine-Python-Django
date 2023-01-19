from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ex00(request):
    return render( request, "index.html" )