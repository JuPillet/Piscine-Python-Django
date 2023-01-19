import pickle
import requests

from worldmap.options import *
from random import randint

class Content:

	url = 'http://www.omdbapi.com/?apikey=dd301a39&t='

	def __init__(self):
		self.grid_size = grid_size
		self.movies = movies
		self.pos = pos
		self.strength = 0
		self.movieballs = 0
		self.filmsContents = []
		with open('data/film_data.txt', 'wb') as fd: # truncate
			pass

		fd = open('data/film_data.txt', 'ab+')
		for e in movies:
			finalUrl = self.url + e.lower().replace(' ', '+')
			r = requests.get(finalUrl)
			#r.text += {'caught' : False}
			self.filmsContents.append(r.text)
			pickle.dump(r.text, fd)
		fd.close()

class Data:

	def __init__(self):
		self.content = Content()

	def load(self, content : Content):
		self.content = content
	
	def dump(self):
		return self.content

	def get_random_movie(self):
		while True:
			i = randint(0, len(movies)-1)
			if (self.content.filmsContents[i]['caught'] == False):
				return self.content.filmsContents[i]

	def load_default_settings(self):
		self.content = Content()
		return self

	def get_strength(self):
		return self.content.strength

	def get_movie(self, title):
		for e in self.content.filmsContents:
			if (e['title'] == title):
				return e
		return None

d = Data()