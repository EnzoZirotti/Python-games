#Always import library's first.
import pgzrun
from random import  randint

apple = Actor("apple")

# Drawing the apple on the screen

def draw():
    screen.clear()
    apple.draw()
# Defining the function to place the apple
def place_apple():
    apple.x = randint(10, 500)

    apple.y = randint(10, 500)

def on_mouse_down(pos):
    #adding some logic to the button clicks
    if apple.collidepoint(pos):
        print("Good Shot!")
        place_apple()
    else:
        print("You missed!")
        #quit()

place_apple()

pgzrun.go()