import pgzrun
from random import  randint
# Setting the size of the playing area
WIDTH = 400
HEIGHT = 400

# Setting the score
score = 0
game_over = False

# Introducing the Actors
fox = Actor("fox")
fox.pos = 100, 100


coin = Actor("coin")
coin.pos = 200, 200
# Display the Actors on the screen
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(101, 10)) 


pgzrun.go()
