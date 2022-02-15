import pgzrun
import random


FONT_COLOR = (255, 255, 255)

WIDTH = 800

HEIGHT = 600

CENTER_X = WIDTH / 2

CENTER_Y = HEIGHT / 2

CENTER = (CENTER_X, CENTER_Y)

FINAL_LEVEL = 6

START_SPEED = 10

COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []
## Drawing the stars
def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0,0))
    if game_over:
        display_message("Game Over!", "Try Again")
    elif game_complete:
        display_message("YOU WON!!", "Well Done")
    else:
        for star in stars:
            star.draw()
## Define the update function

def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

## Make the stars

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

