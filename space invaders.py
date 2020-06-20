#space invaders attempt

import turtle
import random

width = 650
height = 1050
bg = "black"
fg = "white"
title = 'Space Invaders Clone'
bdrwidth = 3
playerspeed = 15
buffer = 0.46


#create the screen
scrn = turtle.Screen()
scrn.bgcolor(bg)
scrn.title(title)

	

#create the border
def draw_border(color):
	border_pen = turtle.Turtle()
	border_pen.speed(0)
	border_pen.color(color)
	border_pen.up()
	border_pen.hideturtle()
	border_pen.pensize(bdrwidth)
	border_pen.setx(-width/2)
	border_pen.sety(-height/2)
	border_pen.down()
	for side in range(4):
		if side % 2 == 0:
			border_pen.forward(width)
		else:
			border_pen.forward(height)
		border_pen.lt(90)


player = turtle.Turtle()
player.speed(0)
player.up()
player.color(fg)
player.sety(-height*buffer)
player.lt(90)

#move player left
def moveleft():
	player.setx(player.xcor()-playerspeed)
	if player.xcor() < (-width * buffer):
		player.setx(-width * buffer)

#move player right
def moveright():
	player.setx(player.xcor()+ playerspeed)
	if player.xcor() > (width * buffer):
		player.setx(width * buffer)

def getclickcoor(x,y):
#	player.goto(x,y)
#	moveright()
	if x > 20:
		moveright()
	if x < -20:
		moveleft()


draw_border(fg)
scrn.onclick(getclickcoor)
scrn.listen()


	
turtle.mainloop()