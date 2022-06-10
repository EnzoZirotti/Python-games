from pickle import TRUE
import pgzrun
from random import randint


WIDTH = 800
HEIGHT = 600


balloon = Actor("balloon")
balloon.pos = 400, 300


#Preparing obsacles


bird = Actor("bird-up")
bird.pos = randint(800, 1600), 460


house = Actor("house")
house.pos = randint(800, 1600), 460


tree = Actor("tree")
tree.pos = randint(800, 1600), 450


bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0


scores = []