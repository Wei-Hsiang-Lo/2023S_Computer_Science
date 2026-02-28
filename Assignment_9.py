#I write this program by myself. Sign here: 羅瑋翔
#Email address: xianglo9121.mg10@nycu.edu.tw
#Anything special? Let people easily understand my code with the comment
#I provided special function. (1)讓cantor dust依不同depth漸層，並讓使用者選擇不同顏色的漸層 
import turtle
import math

def applyProduction(axiom, rules, depth):
    autoApplied = axiom
    for i in range(depth):
        newString = ""
        for ch in autoApplied:
            newString = newString + rules.get(ch, ch)
        autoApplied = newString
    return autoApplied

def drawLS(t, instructions, angle, d):
    stateSaver = []
    t.speed(10)
    for cmd in instructions:
        if cmd == 'F':
            t.forward(d)
        elif cmd == 'B':
            t.backward(d)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == '[':
            pos = t.position()
            head = t.heading()
            stateSaver.append((pos, head))
        elif cmd ==']':
            (pos, head) = stateSaver.pop()
            t.up()
            t.setposition(pos)
            t.setheading(head)
            t.down()
        elif cmd == ' ':
            t.up()
            t.forward(d)
            t.down()

#(1) This part of program is used to draw sierpinski triangle
def drawTriangle(t, p1, p2, p3, color):
    t.color(color)
    t.speed(10)
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)

def getMidPoint(p1, p2):
    midX = (p1[0] + p2[0]) / 2
    midY = (p1[1] + p2[1]) / 2
    midPoint = [midX, midY]
    return midPoint

def sierpinski(t, p1, p2, p3, depth, color):
    if depth > 0:
        for i in range(3):
            color[i] = color[i] + 5
        sierpinski(t, p1, getMidPoint(p1, p2), getMidPoint(p1, p3), depth - 1, color)
        sierpinski(t, getMidPoint(p1, p2), p2, getMidPoint(p2, p3), depth - 1, color)
        sierpinski(t, getMidPoint(p1, p3), getMidPoint(p2, p3), p3, depth - 1, color)
    else:   
        drawTriangle(t, p1, p2, p3, color)
    
#(2) This part of program is used to draw snowflake
def lsystem_1(axiom, rules, depth, angle, d):
    edge = d * (3 ** (depth - 1))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-30, -edge, edge + 30, 270)

    newRules = applyProduction(axiom, rules, depth)
    #write a list to store the initial position, and use them in a for loop
    iniPositionList = [[0, 0], [edge, 0], [edge / 2, math.sqrt(3) / 2 * (-edge)]]

    for i in range(3):
        t.color(0, 178, 238)
        t.up()
        t.setposition(iniPositionList[i])
        t.setheading(-120 * i)
        t.down()
        drawLS(t, newRules, angle, d)
    
    t.hideturtle()
    wn.exitonclick()

#(3) This part of program is used to draw rosemary
def lsystem_2(axiom, rules, depth, iniPosition, iniHeading, angle, d):
    t = turtle.Turtle()
    wn = turtle.Screen()
    #change the color of rosemary
    t.color(34, 139, 34)
    t.up()
    t.setposition(iniPosition)
    t.setheading(iniHeading)
    t.down()

    newRules = applyProduction(axiom, rules, depth)
    drawLS(t, newRules, angle, d)

    t.hideturtle()
    wn.exitonclick()

#(4) This part of program is used to draw Cantor dust
def lsystem_3(axiom, rules, depth, d):
    newD = d / (3 ** (depth - 1))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-10, -10, d + 30, d + 30)
    angle = 0
    #讓使用者選擇做漸層的顏色
    colorChoice = int(input("1 for blue gradient.\n2 for red gradient.\n3 for gray gradient.\n4 for green gradient.\n5 for purple gradient.\nPlease enter your choice of color(1~5) : "))
    if choice < 1 or choice > 5:
        print("Invalid value for color choice.")
    print("Yout choice is :", colorChoice)
    
    blueList = [[0, 0, 255], [0, 0, 220], [0, 0, 205], [0, 0, 175], [0, 0, 145], [0, 0, 115]]
    redList = [[255, 128, 0], [255, 69, 0], [255, 0, 0], [238, 0, 0], [205, 0, 0], [139, 0, 0]]
    grayList = [[40, 40, 40], [70, 70, 70], [100, 100, 100], [130, 130, 130], [160, 160, 160], [190, 190, 190]]
    greenList = [[0, 255, 0], [0, 238, 0], [0, 205, 0], [0, 175, 0], [0, 145, 0], [0, 0, 115]]
    purpleList = [[171, 130, 255], [159, 121, 238], [123, 104, 238], [137, 104, 205], [125, 38, 205],  [93, 71, 139]]
    
    for i in range(1, depth + 1):
        if colorChoice == 1:
            t.color(blueList[i-1])
        elif colorChoice == 2:
            t.color(redList[i-1])
        elif colorChoice == 3:
            t.color(grayList[i-1])
        elif colorChoice == 4:
            t.color(greenList[i-1])
        elif colorChoice == 5:
            t.color(purpleList[i-1])
            
        newD = d / (3 ** (i - 1))
        t.up()
        t.setposition((0, 300 - (60 * (i - 1))))
        t.down()
        newRules = applyProduction(axiom, rules, i)
        drawLS(t, newRules, angle, newD)

    t.hideturtle()
    wn.exitonclick()

#this is the main funciton to let the users choose which
choice = int(input("1 to draw sierpinski triangle\n2 to draw snowflake\n3 to draw rosemary\n4 to draw a Cantor dust\nEnter your choice to draw the picture : "))
turtle.colormode(255)
#by the choice, enter the corresponded funciton to draw the figure
if choice == 1:
    side = 100
    p1 = [0, 0]
    p2 = [side, 0]
    p3 = [side / 2, math.sqrt(3) / 2 * side]
    depth = 4
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-10, -10, side + 10, side + 10)
    color = [10, 10, 10]
    sierpinski(t, p1, p2, p3, depth, color)
    t.hideturtle()
    wn.exitonclick()#not done(need to change color)

elif choice == 2:
    d = 10
    angle = 60
    depth = 5
    axiom = 'X'
    snowflakeRules = {'X':'F',
                      'F':'F-F++F-F'}
    lsystem_1(axiom, snowflakeRules, depth, angle, d)
    
elif choice == 3:
    d = 5
    angle = 25.7
    depth = 5
    axiom = 'H'
    rosemaryRules = {'H':'HFX[+H][-H]',
                     'X':'X[-FFF][+FFF]FX'}
    lsystem_2(axiom, rosemaryRules, depth, (0, -200), 90, angle, d)

elif choice == 4:
    d = 300
    depth = 6
    axiom = 'X'
    cantorDustRules = {'X':'F',
                       'F':'F F',
                       ' ':'   '}
    lsystem_3(axiom, cantorDustRules, depth, d)
    
else:
    print("Invalid value for choice.")
