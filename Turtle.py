import turtle
turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor('red')

while True:
    
    angle = int(input("거북이의 회전 각도: "))
    distance = int(input("거북이가 이동할 거리: "))
    turtle.right(angle)
    turtle.forward(distance)

turtle.exitonclick()