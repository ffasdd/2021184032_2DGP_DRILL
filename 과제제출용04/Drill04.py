import turtle

num = 5
count = 5
i=0

while(num>0):
    count=5
    while (count > 0) :
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        count-=1
    num-=1
    i = 5-num
    turtle.penup()
    turtle.goto(0,i*100)
    turtle.pendown()
   

