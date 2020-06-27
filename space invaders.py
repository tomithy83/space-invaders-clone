#space invaders attempt

import turtle
import random
import math

width = 650
height = 1050
bg = "black"
fg = "white"
title = 'Space Invaders Clone'
bdrwidth = 3
playerspeed = 15
buffer = 0.46
numofenemies = 20
enemies =[]

#create the screen
scrn = turtle.Screen()
scrn.bgcolor(bg)
scrn.title(title)
scrn.tracer(0)

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
	
	def __init__(self, color, shape='triangle',x=0, y=(-height*buffer)):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.up()
		self.t.shape(shape)
		self.t.shapesize(1.5,1.5)
		self.t.color(color)
		self.t.goto(x,y)
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
	
	def __init__(self,color,shape,x=(-width*buffer),y=(height*buffer),state='alive'):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.up()
		self.t.shape(shape)
		self.t.color(color)
		self.t.goto(x,y)
		self.state = 'alive'
		
	def movement(self):
		self.t.setx(self.t.xcor()+ enemy.enemyspeed)
		if self.t.xcor() > width*buffer:
			for i in enemies:
				i.t.goto(i.t.xcor() -2, i.t.ycor() - 20)
			enemy.enemyspeed *= (-1)
		if self.t.xcor() < -width*buffer:
			for i in enemies:
				i.t.goto(i.t.xcor() +2, i.t.ycor() - 20)
			enemy.enemyspeed *= (-1)
			
	def enemydestruction(self):
		self.state = 'dead'
		self.t.goto(-10000,0)
			
			
		
			
class bullet:
	bulletspeed = 20
	def __init__(self,color,shape='triangle',x=10000,y=0,speedmultiplyer=1):
		self.t = turtle.Turtle()
		self.t.speed(0)
#		self.t.hideturtle()
		self.t.up()
		self.t.shape(shape)
		self.t.shapesize(0.5,0.5)
		self.t.color(color)
		self.t.goto(x,y)
		self.t.state = 'ready'
		self.t.speedmultiplyer = speedmultiplyer
		if speedmultiplyer >= 0:
			self.t.lt(90)
		else:
			self.t.lt(270)
		
	def firebullet(self,origin):
		if self.t.state == 'ready':
			self.t.state ='fire'
			self.t.goto(origin.t.xcor(),origin.t.ycor())
			self.t.showturtle()
		
	def movebullet(self):
		if self.t.state == 'fire':
			newy= self.t.ycor()+(bullet.bulletspeed*self.t.speedmultiplyer)
			self.t.sety(newy)
		if self.t.ycor() > height*buffer:
#			drwmsg('passed boundry')
			self.resetbullet()
	
	
	def resetbullet(self):
		self.t.state = 'ready'
		self.t.goto(10000,0)
			
	
def getclickcoor(x,y):
#	drwmsg('the click registered x: ' + str(x) + 'y: ' + str(y))
	playerbullet1.firebullet(player1)
	if x > 20:
		player1.moveright()
#		drwmsg('>20')
	if x < -20:
		player1.moveleft()
#		drwmsg('<-20')

#check for collisions between turtles
def iscollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance <15:
		#drwmsg('True')
		return True
	else:
		#drwmsg('False')
		return False
	#drwmsg(distance)
	
	
	
#create player bullet
playerbullet1 = bullet('yellow')

#create player1
player1 = player(fg)
#drwmsg(player1.__dict__)

#create enemies
#enemy1 = enemy('red','circle')
#drwmsg(enemy1.__dict__)
for i in range(numofenemies):
	enemyx = (-width*buffer)+(30*(i%5))
	enemyy = (height*buffer)-(30*math.floor(i/5))
	i = enemy('red','circle',x=enemyx,y=enemyy)
	enemies.append(i)
	
	
#for enemy in enemies:
#	enemy = enemy('red','circle',x=(-width*buffer)+(I*30),y=(height*buffer)
#	drwmsg(enemies)


draw_border(fg)
scrn.onclick(getclickcoor)
scrn.listen()


	
while True:
	for i in enemies:
		if i.state == 'alive':
			i.movement()
		if iscollision (i.t, playerbullet1.t):
			playerbullet1.resetbullet()
			i.enemydestruction()

	playerbullet1.movebullet()
	scrn.update()
	continue