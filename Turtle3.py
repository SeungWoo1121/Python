import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("blue")

turtle.screensize(300, 300)
turtle.setup(330, 330)

while True:
    angle = random.randint(0, 360) # 0도에서 360도 까지 랜덤으로 돌음
    distance = random.randint(10, 100) # 10에서 100사이 이동할 거리
    turtle.right(angle) # 오른쪽으로 돌기
    turtle.forward(distance) # 앞으로 가기

    curX = turtle.xcor() # 거북이의 현재 x좌표 반환
    curY = turtle.ycor() # 거북이의 현재 y좌표 반환

    if (curX >= -150 and curX <= 150 ) and (curY >= -150 and curY <= 150):
        print("Go!")
    else:
        turtle.goto(0,0)
        print("go to origin")

turtle.done()