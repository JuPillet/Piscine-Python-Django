from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm
import logging

def form( request ):
	if ( request.method == "POST" ):
		form = MyForm( request.POST )
		if form.is_valid():
			logger = logging.getLogger( "formLogger" )
			logger.debug( form.cleaned_data['input'] )
			form = MyForm()
	else:
		form = MyForm()
	return render( request, "form.html", {'form': form } )
	