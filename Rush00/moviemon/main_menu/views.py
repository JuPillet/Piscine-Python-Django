from django.shortcuts import render
from moviemon.data import Data

# Create your views here.


def menu(request):
	return render(request, 'gameboy.html')