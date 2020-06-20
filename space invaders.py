#space invaders attempt

import turtle
import random

width = 650
height = 1050
bg = "black"
fg = "white"
title = 'Space Invaders Clone'
bdrwidth = 3



def newscreen(color, name):
	#create the screen
	scrn = turtle.Screen()
	scrn.bgcolor(color)
	scrn.title(name)

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

def mkplayer(color,speed):
	player = turtle.Turtle()
	player.speed(0)
	player.up()
	player.color(color)
	player.sety(-height*7/16)
	player.lt(90)
	playerspeed = speed

#move player left
def moveleft():
	player.setx(player.corx()-playerspeed)
	if player.corx() < (-width * 7/16):
		player.setx(-width * 7/16)

#move player right
def moveright():
	player.setx(player.corx()+playerspeed)
	if player.corx() < (width * 7/16):
		player.setx(width * 7/16)

newscreen(bg,title)
draw_border(fg)
mkplayer(fg,15)


while True:
	continue
	