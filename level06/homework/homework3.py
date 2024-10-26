from turtle  import *
# Drawing the flag of Georgia

#Step 1:Making the outline
width(7)
forward(500)
left(90)

forward(300)
left(90)

forward(500)
left(90)

forward(300)
left(90)

#Step 2:Drawing the crosses
forward(250)

width(15)
color("red")
left(90)
forward(300)

penup()
goto(0,150)
pendown()

right(90)
forward(500)

#Making small crosses

#1
penup()
goto(125,225)
pendown()

left(90)
forward(45)
left(180)
forward(90)


penup()
goto(80,225)
pendown()

left(90)
forward(90)

#2
penup()
goto(375,270)
pendown()

right(90)
forward(90)

penup()
goto(330,225)
pendown()

left(90)
forward(90)

#3
penup()
goto(125,30)
pendown()

left(90)
forward(90)

penup()
goto(80,75)
pendown()

right(90)
forward(90)

#4
penup()
goto(375,30)
pendown()

left(90)
forward(90)

penup()
goto(330,75)
pendown()

right(90)
forward(90)





exitonclick()