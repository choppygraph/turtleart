import turtle
import random
turtle.penup()
turtle.goto(0,0)
forward=200
sen=1
right=0
color=0
turtle.right(0)
turtle.speed(10)
num1=random.randint(0,0)
num2=random.randint(10,360)
print(num1)
print(num2)
while sen==1:
  num3=random.randint(1,10)
  color=color+1
  if color==1:
    if num3==1:
      turtle.fillcolor("CornflowerBlue")
    elif num3==2:
      turtle.fillcolor("DarkOrchid4")
    elif num3==3:
      turtle.fillcolor("SeaGreen3")
    elif num3==4:
      turtle.fillcolor("DeepSkyBlue")
    elif num3==5:
      turtle.fillcolor("SlateBlue2")
    elif num3==6:
      turtle.fillcolor("DodgerBlue3")
    elif num3==7:
      turtle.fillcolor("MediumSpringGreen")
    elif num3==8:
      turtle.fillcolor("SteelBlue1")
    elif num3==9:
      turtle.fillcolor("purple1")
    elif num3==10:
      turtle.fillcolor("MediumPurple")
    turtle.begin_fill()
  elif color==3:
    color=color-3
    turtle.end_fill()
  turtle.fd(forward+num1)
  turtle.right(right+num2)
  forward=forward*.99
  if forward+num1>30:
    forward=forward+0
  right=right+0
  if right+num2<20:
    right=right+.0
  elif right>360:
    right=right-0
