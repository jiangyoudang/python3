import random
import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.screensize(800,600,'lightgreen')

def tree(branchlen,t):
    # rand = random.randint(10,25)

    if branchlen >5:
        pen.pensize(branchlen/10)
        head = t.heading()
        t.forward(branchlen)
        # t.right(random.randint(20,45))
        t.right(random.randint(5,20))
        tree(branchlen-random.randint(10,15),t)
        t.setheading(head)
        t.left(random.randint(5,20))
        # t.left(random.randint(20,45))
        tree(branchlen-random.randint(10,15),t)
        t.setheading(head)
        t.backward(branchlen)

pen = turtle.Turtle()
pen.color('hotpink')
pen.up()
pen.goto(0,-250)
pen.left(90)
pen.down()
pen.speed(10)
tree(100,pen)

#tess = turtle.Turtle()           # create tess and set some attributes
#tess.color("hotpink")
#tess.pensize(5)
#
#tess.forward(80)                 # Let tess draw an equilateral triangle
#tess.left(120)
#tess.forward(80)
#tess.left(120)
#tess.forward(80)
#tess.left(120)                   # complete the triangle
#
#tess.right(180)                  # turn tess around
#tess.forward(80)
wn.exitonclick()


# print(True ^ True)

