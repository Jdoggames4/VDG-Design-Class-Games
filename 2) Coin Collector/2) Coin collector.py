# Jacob Dinkel

from random import randint

WIDTH = 800
HEIGHT = 400

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100,100
fox.speed = 20

coin = Actor("coin")
coin.pos = 200,200

def draw():
    screen.fill("dimgray")
    fox.draw()
    coin.draw()

    screen.draw.text("Score: " + str(score),
                            color = "azure",
                            topleft = (10,10))

    if game_over:
        screen.fill("slategray")
        screen.draw.text("Final Score: " +  str(score),
                                    color = "darkgrey",
                                    center = (400,200),
                                    fontsize = 150)

def place_coin():
    coin.x = randint (20, (WIDTH -20))
    coin.y = randint (20, (HEIGHT -20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.a:
        fox.x = fox.x - 2
    elif keyboard.d:
        fox.x = fox.x + 2
    elif keyboard.w:
        fox.y = fox.y - 2
    if keyboard.s:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 15
        place_coin()

clock.schedule(time_up, 50.0)

