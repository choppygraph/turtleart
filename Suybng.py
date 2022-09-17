import turtle
import random

function draw(forward, right):
    turtle.forward(num1+forward)
    turtle.left(num2+right)


forward=0
sen=1
right=0
turtle.speed(5)
num1=random.randint(1,10)
num2=random.randint(-10,10)
while sen==1:
    draw(forward, right)
    forward=forward+1
    right=right+1

