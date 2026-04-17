# Jacob Dinkel
# Treasure Hunt

from random import randint
from pgzhelper import *

# Screen
WIDTH = 1000
HEIGHT = 600
TITLE = "Tresure Hunt"
ICON = "ship"

# Colors
CADETBLU = "cadetblue"
MEDIUMVI = "mediumvioletred"
WHITE = "white"

# Game
score = 0
lives = 10
game_over = False
over_sound = False

# Images
bg = Actor("background")

ship = Actor("ship")
ship.x = 400
ship.y = 550

coin = Actor("coin")
coin.x = randint(20, 780)
coin.y = 0

skull = Actor("skull")
skull.x = randint(20, 780)
skull.y = 0

bomb = Actor("bomb")
bomb.x = randint(20, 780)
bomb.y = 0


def update():
    global score
    global lives
    global game_over
    global over_sound

    if keyboard.a:
        ship.x -= 5
        ship.flip_x = False
    if keyboard.d:
        ship.x += 5
        ship.flip_x = True
    if keyboard.left:
        ship.x -= 5
        ship.flip_x = False
    if keyboard.right:
        ship.x += 5
        ship.flip_x = True

    if keyboard.left and keyboard.space:
        ship.x -= 10
    if keyboard.right and keyboard.space:
        ship.x += 10
    if keyboard.a and keyboard.space:
        ship.x -= 10
    if keyboard.d and keyboard.space:
        ship.x += 10

    if ship.x < 60:
        ship.x = 60
    if ship.x > 940:
        ship.x = 940

    coin.y += 4 + score / 62
    if coin.y > 600:
        coin.x = randint(20, 940)
        coin.y = 0
    if coin.colliderect(ship):
        sounds.collect.play()
        coin.x = randint(20, 840)
        coin.y = 0
        score += 3

    skull.y += 4 + score / 32
    if skull.y > 600:
        skull.x = randint(20, 780)
        skull.y = 0
    if skull.colliderect(ship):
        sounds.lose.play()
        skull.x = randint(20, 780)
        skull.y = 0
        score -= 1

    bomb.y += 4 + score / 32
    if bomb.y > 600:
        bomb.x = randint(20, 780)
        bomb.y = 0
    if bomb.colliderect(ship):
        sounds.explosion.play()
        bomb.x = randint(20, 780)
        bomb.y = 0
        lives -= 1

    if lives == 0:
        game_over = True
        coin.y = 0
        skull.y = 0
        bomb.y = 0
        if over_sound == False:
            sounds.gameover.play()
        over_sound = True


def draw():
    bg.draw()
    if game_over:
        screen.draw.text("GAME OVER!",
                        (230, 200),
                        color = WHITE,
                        fontname = "publicpixel",
                        fontsize = 30)
        screen.draw.text("Final Score: " + str(score),
                        (180, 300),
                        color = WHITE,
                        fontname = "publicpixel",
                        fontsize = 30)

    else:
        ship.draw()
        coin.draw()
        skull.draw()
        bomb.draw()
        screen.draw.text("Score: " + str(score),
                        (875, 10),
                        color = (CADETBLU),
                        fontname = "publicpixel",
                        fontsize = 15)
        screen.draw.text("Lives: " + str(lives),
                        (8, 10),
                        color = (MEDIUMVI),
                        fontname = "publicpixel",
                        fontsize = 15)
