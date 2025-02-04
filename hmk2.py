import pgzrun
from random import randint

SCREEN=400
WIDTH=400
TITLE="Circle Pattern"

def draw():
    screen.fill("black")
    r=255
    g=0
    b=randint(60,255)
    size=30

    for i in range(5):
        screen.draw.circle((200,200),size,(r,g,b))
        size=size+10
        r=r-20
        g=g+20
pgzrun.go()