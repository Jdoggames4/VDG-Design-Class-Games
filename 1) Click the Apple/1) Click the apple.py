# Jdoggames4
# Click the Apple

from random import randint

WIDTH = 800
HEIGHT = 500
score = 0
game_over = False


apple = Actor("apple")

def on_mouse_down(pos):
    global score

    if not game_over:
        if apple.collidepoint(pos):
            score = score + 250
            print("Good Job!")
            place_apple()
        else:
            score = score - 150
            print("You Missed!")
            place_apple()

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,400)

def end_the_game():
    global game_over
    game_over = True

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score),
                          topleft = (10,10),
                              fontsize = 30,
                             color = "snow")

    if game_over:
        screen.fill("mediumvioletred")
        screen.draw.text("Final Score: " + str(score),
                                   center = (400,250),
                                       fontsize = 150,
                                   color = "lavenderblush")

clock.schedule(end_the_game, 35.0)
clock.schedule_interval(place_apple, 2.0)



place_apple()



