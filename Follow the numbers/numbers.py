import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
# Setting up lists
dots = []
lines = []


next_dot = 0
# Set up the actors
for dot in range(0, 10):
    
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), \
    randint(20, HEIGHT - 20)
    dots.append(actor)

# Draw the actors

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dont.pos[1] + 12))

        dot.draw()
        number = number + 1
    
    # Draw the lines
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
