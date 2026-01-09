from turtle import forward,left,right,exitonclick
from math import sqrt

global a
global b
a=int(input("how big is the house? : "))

def turn():
    b=30
    right(b)
def domecek():
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    right(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    right(45)
    forward((sqrt(2*a**2))/2)
    right(90)
    forward((sqrt(2*a**2))/2)
    right(45)
    forward(a)
    left(90)
def final():
    domecek()
    turn()

final()
final()
final()
final()
final()
final()
final()
final()
final()
final()
final()
final()

exitonclick()
