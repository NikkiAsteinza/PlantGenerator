#from joblib import Parallel, delayed
#import multiprocessing
import turtle
import random
import os
import time
#Path
currentpath= os.path.dirname(os.path.realpath(__file__))
screen = turtle.Screen()
#Tamaño de la ventana
screen.setup(445, 255)
#Tamaño del lienzo
screen.screensize(445, 250)
#Fondo de Pantalla
bg =currentpath+r"\background.gif"
#Cambiar Fondo
screen.bgpic(bg)
screen.update
#Titulo de la ventana
screen.title("Generador de plantas - Nikki Asteinza")
#Fondo de la ventana
screen.bgcolor("black");
#Velocidad de movimiento
move_speed =50
#Nucleos
#threads = multiprocessing.cpu_count()
variables = ['F','X']
regla = ["F", "F[-FX]F[+FX][F]"]
axioma = "X"

height = 10
turn = 30
stack = []
dirstack = []
pens = []
#Main
pens.append(turtle.Turtle())
pens[0].pencolor("green")
pens[0].left(90)
pens[0].penup()
pens[0].setpos(0, -120)
pens[0].pendown()
pens[0].shape("turtle")
pens[0].pensize(2)
mainPSize =pens[0].pensize()
#Pen2
pens.append(turtle.Turtle())
pens[1].pencolor("#ffd800")
rnd = random.uniform(-0.1, 0.1)
posVariation = mainPSize-(1+ rnd)
pens[1].left(90-posVariation)
pens[1].penup()
pens[1].setpos(0, -120)
pens[1].pendown()
pens[1].shape("turtle")
pens[1].pensize(2)
#Pen3
pens.append(turtle.Turtle())
pens[2].pencolor("#14a81b")
rnd = random.uniform(-0.2, 0.2)
posVariation = mainPSize - rnd
pens[2].left(90-posVariation)
pens[2].penup()
pens[2].setpos(0, -120)
pens[2].pendown()
pens[2].shape("turtle")
pens[2].pensize(1)

def generate(iteration):
	result = axioma
	temp = ""
	for i in range(iteration):
		for j in range(len(result)):
			for k in range(len(variables)):
				if (result[j] == variables[k]):
					temp += regla[k]
					break
				if (k == len(variables)-1):
					temp += result[j]
		result = temp
		temp = ""
	return result
def draw(input,pen):
	p= pen
	p.speed(move_speed)
	for x in input:
		if (x == 'F'):
			p.forward(height)
		elif (x == '-'):
			p.left(turn)
		elif (x == '+'):
			p.right(turn)
		elif (x == '['):
			stack.append(p.pos())
			dirstack.append(p.heading())
		elif (x == ']'):
			p.penup()
			post = stack.pop()
			direc = dirstack.pop()
			p.setpos(post)
			p.setheading(direc)
			p.pendown()
	p.hideturtle()
input= generate(6);
for p in pens:
	draw(input,p)
time.sleep(2.4)
