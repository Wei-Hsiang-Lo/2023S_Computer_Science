#I write this programby myself. Sign here:羅瑋翔
#Email Address: xianglo9121.mg10@nycu.edu.tw
#Anything sjpecial? I remind the users to enter what data type should be entered.
#I provided addtional functions: None
import math
import random
import turtle

def func(parS, x0,terms):
    xn = (x0+(parS/x0))/2
    return xn

def showMontePi(n):
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.setworldcoordinates(-2, -2, 2, 2)

    #draw the horizontal axis
    t.up()
    t.goto(-1, 0)
    t.down()
    t.goto(1, 0)

    #draw the vertical axis
    t.up()
    t.goto(0, 1)
    t.down()
    t.goto(0, -1)

    inCircle = 0
    t.up()
    for i in range(n):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        if d <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")
        t.goto(x,y)
        t.dot()
        t.speed(0)

    pi = inCircle/n*4
    wn.exitonclick()
    return pi

print("The purpose of this program is to compare the result with different x0")
s = float(input("Enter the value of s for the first function (real number):"))
terms = int(input("and enter the terms for the first function (int):"))
x0 = float(input("Enter the value of x0 for the second function (real number):"))
print("The value of s = ", s, ", x0 = ", x0, ", terms_2 = ", terms)

resFun1 = 1.0
for i in range(terms):
    temp_1 = func(s, resFun1, terms)
    resFun1 = temp_1
for i in range(terms):
    temp_2 = func(s, x0, terms)
    x0 = temp_2

xn = math.sqrt(s)
print("The value of Xn computed with funtion1 = %.15f" % (resFun1) )
print("The value of Xn computed with funtion2 = %.15f" % (x0))
print("The value with the sqrt function provided by python = %.10f" % (xn))
showMontePi(200)
