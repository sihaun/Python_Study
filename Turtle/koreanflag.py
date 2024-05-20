import turtle
diameter = 24*10 # 지름을 기준으로 단위 설계

t = turtle.Turtle()
t.penup()
t.setheading(90) # 정면을 바라보게 초기 설정

def jump(): # 단위 간격 점프
    t.forward(diameter/8)

def regration(): # 건곤감리를 그리고 중심으로 회귀하는 함수
    t.left(180)
    t.forward(diameter)

def longBox(): # 긴 검은 막대
    t.pendown()
    t.right(90)
    for _ in range(2):
        t.forward(diameter/4)
        t.left(90)
        t.forward(diameter/12)
        t.left(90)
        t.forward(diameter/4)
    t.left(90)
    t.penup()

def shortTwoBox(): # 짧은 검은 막대 2개
    t.right(90)
    t.forward(diameter/48) # 막대 간격 점프
    t.pendown()
    t.forward(diameter/4 - diameter/48) # 짧은 막대 길이
    t.left(90)
    t.forward(diameter/12)
    t.left(90)
    t.forward(diameter/4 - diameter/48)
    t.left(90)
    t.forward(diameter/12)
    t.penup()
    t.right(90)
    t.forward(diameter/24)
    t.pendown()
    t.forward(diameter/4 - diameter/48)
    t.right(90)
    t.forward(diameter/12)
    t.right(90)
    t.forward(diameter/4 - diameter/48)
    t.right(90)
    t.forward(diameter/12)
    t.left(90)
    t.forward(diameter/48)
    t.penup()
    t.left(90)

def taegeuk(): # 태극 문양
    t.right(45)
    t.circle(diameter/4, 180)
    t.pendown()
    t.circle(diameter/4, 180)
    t.penup()
    t.right(180)
    t.circle(diameter/4, 180)
    t.pendown()
    t.circle(diameter/4, 180)
    t.penup()
    t.right(90)
    t.forward(diameter/2)
    t.left(90)
    t.pendown()
    t.circle(diameter/2)
    t.penup()
    t.left(180)
    t.left(45)

def koreanflag(): # 태극기 전체를 그리는 함수
    taegeuk()
    t.left(45)
    jump()
    for _ in range(3): #건
        jump()
        longBox()

    regration()
    t.right(90)
    t.forward(diameter*3/4)
    #감
    longBox()
    jump()
    shortTwoBox()
    jump()
    longBox()

    regration()
    t.forward(diameter*3/4)
    #곤
    shortTwoBox()
    jump()
    longBox()
    jump()
    shortTwoBox()

    regration()
    t.left(90)
    t.forward(diameter*3/4)
    #리
    for _ in range(3):
        shortTwoBox()
        jump()




def main():
    koreanflag()

if __name__ == "__main__":
    main()




