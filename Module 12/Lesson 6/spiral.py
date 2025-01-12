import turtle

sc=turtle.Screen()
sc.bgcolor("Black")
sc.setup(600,600)
sc.title("Rainbow Spiral")
colors=["red","deeppink3","pink","deeppink4","pink","deeppink4","violet"]


s=turtle.Turtle()
s.hideturtle()

for x in range(150):
    s.pencolor(colors[x%len(colors)])
    s.width(x/100+1)
    s.forward(x)
    s.left(59)
s.right(239)

for r in range(150,0,-1):
    s.pencolor(black)
    s.width(x/100+7)
    s.forward(x)
    s.left(59)

turtle.done()