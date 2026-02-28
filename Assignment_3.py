#I write this program by myself. Sign here: 羅瑋翔
#Email address: xianglo9121.mg10@nycu.edu.tw
#Anything special? I clearly remind the users to enter the right type of input.
#I provide addtional functions: None
def setFormat(inputString_1):
    inputString_1 = inputString_1.capitalize()
    tempStr = inputString_1.split()
    tempStr = ' '.join(tempStr)
    tempStr = tempStr.split(' , ')
    resultStr = ', '.join(tempStr)
    return resultStr
    
def coverDigits(inputString_2):
    tempStr = inputString_2.split()
    eleNum = len(tempStr)
    for i in range (eleNum):
        if tempStr[i].isdigit():
            length = len(tempStr[i])
            tempStr.remove(tempStr[i])
            tempStr.insert(i, length*('x'))
    resultStr = ' '.join(tempStr)
            
    return resultStr

n1 = int(input("Enter how many times do you want to test the first funciton(int): "))
print("You entered :", n1)
n2 = int(input("Enter how many times do you watn to test the second funcion(int): "))
print("YOu entered :", n2)
for i in range (n1):
    str1 = input("Enter the string that you want to test : ")
    print("The string you entered :", str1)
    print("The outputs:")
    print(setFormat(str1))
for i in range (n2):
    str2 = input("Enter the string that you want to test : ")
    print("The string you entered : ", str2)
    print("The outputs:")
    print(coverDigits(str2))
