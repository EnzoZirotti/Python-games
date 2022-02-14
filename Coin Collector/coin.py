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

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize = 60)
# Adding function placeholders

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
def time_up():
    global game_over
    game_over = True
    

def update():

    global score

    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2
    
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        
        score = score + 10
        place_coin()

# Set the timer
clock.schedule(time_up, 20.0)

# Placing the coin
place_coin()

pgzrun.go()
