__author__ = 'congliu'

import turtle

def d3(length, p,turtle,i):
    if i>0:
        turtle.up()
        turtle.goto(p)
        turtle.setheading(0)
        turtle.forward(length/2)
        p2 = turtle.position()
        turtle.left(60)
        turtle.down()
        turtle.fillcolor(color[i-1])
        turtle.begin_fill()
        turtle.forward(length/2)
        turtle.left(120)
        turtle.forward(length/2)
        p1 = turtle.position()
        turtle.left(120)
        turtle.forward(length/2)
        turtle.end_fill()
        d3(length/2,p,turtle,i-1)
        d3(length/2,p1,turtle,i-1)
        d3(length/2,p2,turtle,i-1)



t = turtle.Turtle()
wn = t.getscreen()
wn.setup(0.8,0.8,None,None)

color = ['yellow','green','blue','cyan','violet','red','orange','purple']
t.up()
t.goto((-300,-300))
t.down()
for i in range(3):
    t.forward(600)
    t.left(120)

d3(600,(-300,-300),t,5)
t.speed(10)
wn.exitonclick()