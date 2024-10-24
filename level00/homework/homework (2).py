from turtle import *

#we want to paint a house

# step one: make a square

speed(30)
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of the square

#drawing a door

forward(70)
color("yellow")

begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
  
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#making windows
penup()
goto(60,80)
pendown()

color("green")
begin_fill()
right(60)
forward(55)

right(90)
forward(55)

right(90)
forward(55)

right(90)
forward(55)
end_fill()

penup()
goto(195,80)
pendown()

begin_fill()
right(90)
forward(55)

right(90)
forward(55)

right(90)
forward(55)


right(90)
forward(55)
end_fill()






exitonclick() 



