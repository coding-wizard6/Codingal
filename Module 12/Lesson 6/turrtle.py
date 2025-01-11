import turtle

sc=turtle.Screen()
sc.bgcolor("Green")
sc.setup(600,600)
sc.title("SQUARE")

s=turtle.Turtle()

for i in range(4):
    s.forward(100)
    s.right(90)
    i=i+1

turtle.done()
