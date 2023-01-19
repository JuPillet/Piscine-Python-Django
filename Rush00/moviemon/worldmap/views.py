from django.shortcuts import render
from moviemon.data import Data
import pickle, os
from random import randint

# Create your views here.

def changeMovieball(operation):
	fd_in = open('data/current.mmg', 'rb')
	fd_out = open('data/tmp.txt', 'wb')
	for i in range(5):
		line = pickle.load(fd_in)
		if i == 2:
			balls = int(line)
			if (operation == '+'):
				balls += 1
			toWrite = str(balls)
		else:
			toWrite = line
		if i != 4:
			toWrite += '\n'
		pickle.dump(toWrite, fd_out)
	fd_in.close()
	fd_out.close()
	os.remove('data/current.mmg')
	os.rename('data/tmp.txt', 'data/current.mmg')
		

def movePos(request, direction):
	i = 0
	fd_in = open('data/current.mmg', 'rb')
	fd_out = open('data/tmp.txt', 'wb')
	for i in range(5):
		line = pickle.load(fd_in)
		if i == 0:
			pos = line.strip().split(' ')
			intPos = [int(pos[0]), int(pos[1])]
			if (direction == 'u'):
				intPos[1] -= 1
			elif direction == 'd':
				intPos[1] += 1
			elif direction == 'l':
				intPos[0] -= 1
			elif direction == 'r':
				intPos[0] += 1
			toWrite = str(intPos[0]) + ' ' + str(intPos[1])
		elif i == 1:
			size = line.strip().split(' ')
			toWrite = line
		else:
			toWrite = line
		if i != 4:
			toWrite += '\n'
		pickle.dump(toWrite, fd_out)
	fd_in.close()
	fd_out.close()
	os.remove('data/current.mmg')
	os.rename('data/tmp.txt', 'data/current.mmg')

	lst = [i for i in range(int(size[0]))]
	lst2 = [i for i in range(int(size[1]))]
	return render(request, 'redirect.html', {'posX': intPos[0], 'posY': intPos[1], 'sizeX': lst, 'sizeY': lst2, 'lenX': len(lst)-1, 'lenY': len(lst2)-1 })


def moveUp(request):
	return movePos(request, 'u')

def moveDown(request):
	return movePos(request, 'd')

def moveLeft(request):
	return movePos(request, 'l')

def moveRight(request):
	return movePos(request, 'r')


def menu(request):
	d = Data()
	d.load_default_settings()
	fd = open('data/current.mmg', 'wb')
	pos = str(d.content.pos[0]) + ' ' + str(d.content.pos[1]) + '\n'
	pickle.dump(pos, fd)
	size = str(d.content.grid_size[0]) + ' ' + str(d.content.grid_size[1]) + '\n'
	pickle.dump(size, fd)
	balls = str(d.content.movieballs) + '\n'
	pickle.dump(balls, fd)
	strength = str(d.content.strength) + '\n'
	pickle.dump(strength, fd)
	pickle.dump(d.content.filmsContents, fd)
	return render(request, 'redirect.html')

def overworld(request):
	fd = open('data/current.mmg', 'rb')
	pos = pickle.load(fd).strip().split(' ')
	size = pickle.load(fd).strip().split(' ')
	balls = int(pickle.load(fd))
	lst = [i for i in range(int(size[0]))]
	lst2 = [i for i in range(int(size[1]))]
	
	event = randint(1, 5)
	fight = False
	phrase = ''
	if (event == 1):
		changeMovieball('+')
		balls += 1
		phrase = 'You found a movieball!'
	

	return render(request, 'worldmap.html', {'posX': int(pos[0]), 'posY': int(pos[1]), 'sizeX': lst, 'sizeY': lst2, 'lenX': len(lst)-1, 'lenY': len(lst2)-1, 'balls': balls, 'phrase': phrase, 'fight': fight })