import pgzrun
from random import randint

#WIDTH AND HEIGHT - sys varbiales - output screen
WIDTH=300
HEIGHT=300
TITLE="Rectangle Pattern"

#draw() - inbuilt func gets called itself. Helps to render animation/shapes/texts...
def draw():
    screen.fill("light blue")

    #Rectangle's height and width
    width=WIDTH
    height=HEIGHT-100
    
    #Rectangle's colour
    r=255
    g=0
    b=randint(120,255)

    for i in range(20):
        #0,0 is started pos of rect
        myRect=Rect((0,0),(width,height))
        myRect.center=150,150
        #Draws rect with size of width and height variables and rgb.
        screen.draw.rect(myRect,(r,g,b))

        width=width-10
        height=height+10

        r=r-10
        g=g+10
    


pgzrun.go()