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

#create the debug pen
debugpen = turtle.Turtle()
debugpen.speed(0)
debugpen.color(fg)
debugpen.hideturtle()
debugpen.up()
#define the debug messaging method
def drwmsg(msg): 
	debugpen.clear()
	debugpen.setposition(-width/2+10, height/2-40)
	debugpen.write(msg)

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

class player:
	playerspeed = 15
	
	def __init__(self, color):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.up()
		self.t.color(color)
		self.t.sety(-height*buffer)
		self.t.lt(90)


	#move player left
	def moveleft(self):
#		drwmsg('move left ' + str(self.t.xcor()))
		self.t.setx(self.t.xcor()-player.playerspeed)
		if self.t.xcor() < (-width * buffer):
			self.t.setx(-width * buffer)
	
	#move player right
	def moveright(self):
#		drwmsg('move right' + str(self.t.xcor()))
		self.t.setx(self.t.xcor()+ player.playerspeed)
		if self.t.xcor() > (width * buffer):
			self.t.setx(width * buffer)

class enemy:
	enemyspeed = 2
	
	def __init__(self,color,shape):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.up()
		self.t.shape(shape)
		self.t.color(color)
		self.t.goto(-width*buffer, height*buffer)
		
	def movement(self):
		self.t.setx(self.t.xcor()+ enemy.enemyspeed)
		if self.t.xcor() > width*buffer:
			self.t.goto(width*buffer -2, self.t.ycor() - 20)
			enemy.enemyspeed *= (-1)
		if self.t.xcor() < -width*buffer:
			self.t.goto(-width*buffer +2, self.t.ycor() - 20)
			enemy.enemyspeed *= (-1)
			
	
	
def getclickcoor(x,y):
	drwmsg('the click registered x: ' + str(x) + 'y: ' + str(y))
	if x > 20:
		player1.moveright()
#		drwmsg('>20')
	if x < -20:
		player1.moveleft()
#		drwmsg('<-20')

player1 = player(fg)
enemy1 = enemy('red','circle')
#drwmsg(player1.__dict__)
draw_border(fg)
scrn.onclick(getclickcoor)
scrn.listen()


	
while True:
	enemy1.movement()
	continue