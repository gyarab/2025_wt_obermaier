import random
from turtle import forward,left,right,exitonclick
from math import sqrt

def turn():
    right(30)

def domecek(size):
    diagonal = sqrt(2 * size**2)
    forward(size)
    left(135)
    forward(diagonal)
    right(135)
    forward(size)
    right(135)
    forward(diagonal)
    right(135)
    forward(size)
    right(45)
    forward(diagonal / 2)
    right(90)
    forward(diagonal / 2)
    right(45)
    forward(size)
    left(90)

def final():
    size = random.randint(1,200)
    domecek(size)
    turn()

for i in range(12):
    final()

exitonclick()