import turtle as t
import math
import time

def drawIt(a, b, n):
    for i in range(n):
        t.fd(a)
        t.right(b)

def judgeNum(num):
    if num % 2:
        return True
    else:
        return False

def main(n):
    a = 180 * (n - 2)#n边形内角
    a1 = 180 * (n / 2 - 2) / (n / 2)#n / 2边形内角
    b = 720 / n#turtle画笔第一次转过的角度
    c = a1 / 2
    if judgeNum(n):
        drawIt(100, b, n)#n为奇数
    else:
        drawIt(100,b, int(n / 2))#n为偶数
        t.penup()
        t.right(c)
        t.fd(50 / math.cos(math.radians(c)))
        t.left(180 - 360 / n)
        t.fd(50 / math.cos(math.radians(c)))
        t.right(180 - c)
        t.pendown()
        drawIt(100, b, int(n / 2))
        
for i in range(3, 50):
    t.penup()
    t.goto(0, 230)
    t.pendown()
    main(i)
    time.sleep(1)
    t.reset()
