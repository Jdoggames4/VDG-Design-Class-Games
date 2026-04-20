# Jdoggames4
# Flappy Bird

import pgzrun
import random
from pgzhelper import *

WIDTH = 640
HEIGHT = 480
TITLE = 'Flappy Bird'

# Ground
ground = Actor("ground")
ground.x = 320
ground.y = 465


# Bird
bird = Actor('bird1')
bird.x = 76
bird.y = 100
bird.images = ["bird1",
               "bird2",
               "bird3",
               "bird4"]
bird.fps = 7.5

# Game over
gameover = Actor("gameover")
gameover.x = 320
gameover.y = 200
gameover.scale = 1

# Variables
gravity = 0.3
bird.speed = 1
bird.alive = True
scroll_speed = -4
score = 0

# Pipes
top_pipe = Actor("top")
bottom_pipe = Actor("bottom")
top_pipe.x = WIDTH
top_pipe.y = -100
gap = 150
bottom_pipe.x = WIDTH
bottom_pipe.y = top_pipe.height + gap



def on_mouse_down():
    global score

    if bird.alive:
        bird.speed = -6.5
        sounds.wing.play()
    else:
        bird.alive = True
        score = 0

def update():
    # Bird
    global score


    bird.animate()
    bird.y += bird.speed
    bird.speed += gravity

    # Game Over
    if bird.y > HEIGHT - 40 or bird.y < 0:
        bird.alive = False
        sounds.die.play()

    # Scroll
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

    # Reset
    if top_pipe.x < -50:
        offset = random.uniform(-100, -200)
        gap = 150
        top_pipe.midleft = (640, offset)
        bottom_pipe.midleft = (640, offset + top_pipe.height + gap)
        score += 1
        sounds.point.play()

    # Collision
    if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
        bird.alive = False
        sounds.hit.play()


def draw():
    # Bg

    screen.blit('bg', (0, 0))

    if bird.alive:

        # Draw
        top_pipe.draw()
        bottom_pipe.draw()
        bird.draw()
        ground.draw()

    else:
        screen.draw.text("Click to play again",
                        color = 'black',
                        center = (320, 300),
                        shadow = (1, 1),
                        scolor = 'red',
                        fontsize = 30)


        gameover.draw()
        bird.x = 75
        bird.y = 100
        gravity = 0
        bird.speed = 0.5

        top_pipe.x = 640
        bottom_pipe.x = 640

    # Score
    screen.draw.text("Score: " + str(score),
                    color = 'white',
                    midtop = (50, 10),
                    shadow = (0.5, 0.5),
                    scolor = 'black',
                    fontsize = 30)
