import turtle

pen = turtle.Turtle()
window = turtle.Screen()


def stickFigure():
    head()
    torso()
    arms()
    legs()


def head():
    for i in range(180):
        pen.forward(2)
        pen.left(2)

def torso():
    pen.right(90)
    pen.forward(150)

def arms():
    pen.right(180)
    pen.forward(75)
    leftArm()
    rightArm()

def leftArm():
    pen.left(90)
    pen.forward(60)
    pen.right(180)
    pen.forward(60)


def rightArm():
    pen.forward(60)
    pen.right(180)
    pen.forward(60)
    pen.left(90)

def legs():
    pen.forward(75)
    rightLeg()
    leftLeg()

def rightLeg():
    pen.left(45)
    pen.forward(60)
    pen.backward(60)

def leftLeg():
    pen.right(90)
    pen.forward(60)



stickFigure()












window.exitonclick()