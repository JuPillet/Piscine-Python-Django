from django.urls import path
from . import views

urlpatterns = [
    path('', views.overworld),
	path('/menu', views.menu),
	path('/up', views.moveUp),
	path('/down', views.moveDown),
	path('/left', views.moveLeft),
	path('/right', views.moveRight),
]