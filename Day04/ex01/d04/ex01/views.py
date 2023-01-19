from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def django(request):
    	return render( request, "django/django.html" )

def display(request):
    	return render( request, "display/display.html" )

def templates(request):
    	return render( request, "templates/templates.html" )