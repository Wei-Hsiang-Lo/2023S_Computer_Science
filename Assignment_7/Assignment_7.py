#I write this program by myself
#Email address: xianglo9121.mg10@nycu.edu.tw
#Anything Special? it is easy to know the what is the function doing throught my content
#None
from image import *
import math

#to Flip through the mid horizontal line
def horizontalFlip(oldImage):
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    newImage = EmptyImage(width, height)
    maxRow = height - 1

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newImage.setPixel(col, maxRow - row, oldPixel)

    return newImage

#to Mirroing the image through the mid horizontal line
def horizontalMirroing(oldImage):
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    maxRow = height - 1
    newImage = EmptyImage(width, height)
    
    if height % 2 == 0:
        horizontalLine = height // 2
    else:
        horizontalLine = height // 2 + 1

    for row in range(horizontalLine):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newImage.setPixel(col, row, oldPixel)
            newImage.setPixel(col, maxRow - row, oldPixel)

    return newImage

#convolve the image which the users want to blur
def blurConvolve(anImage, r, c, mask):
    rowBase = r - 1
    colBase = c - 1
    sumR = 0
    sumG = 0
    sumB = 0
    deno = 0
    for row in range(rowBase, rowBase + 3):
        for col in range(colBase, colBase + 3):
            aPixel = anImage.getPixel(col, row)
            intensityRed = aPixel.getRed()
            intensityGreen = aPixel.getGreen()
            intensityBlue = aPixel.getBlue()
            sumR = sumR + intensityRed * mask[row - rowBase][col - colBase]
            sumG = sumG + intensityGreen * mask[row - rowBase][col - colBase]
            sumB = sumB + intensityBlue * mask[row - rowBase][col - colBase]
            deno = deno + mask[row - rowBase][col - colBase]
            
    red = sumR // deno
    green = sumG // deno
    blue = sumB // deno
    newPixel = Pixel(red, green, blue)
    
    return newPixel

#convolve the image which the users want to sharp
def sharpConvolve(anImage, r, c, mask):
    rowBase = r - 1
    colBase = c - 1
    sumR = 0
    sumG = 0
    sumB = 0
    for row in range(rowBase, rowBase + 3):
        for col in range(colBase, colBase + 3):
            aPixel = anImage.getPixel(col, row)
            intensityR = aPixel.getRed()
            intensityG = aPixel.getGreen()
            intensityB = aPixel.getBlue()
            sumR = sumR + intensityR * mask[row - rowBase][col - colBase]
            sumG = sumG + intensityG * mask[row - rowBase][col - colBase]
            sumB = sumB + intensityB * mask[row - rowBase][col - colBase]
            
    if sumR > 255:
        sumR = 255
    elif sumR < 0:
        sumR = 0
    if sumG > 255:
        sumG = 255
    elif sumG < 0:
        sumG = 0
    if sumB > 255:
        sumB = 255
    elif sumB < 0:
        sumB = 0

    newPixel = Pixel(sumR, sumG, sumB)
    
    return newPixel
    
def blurringImage(anImage):
    width = anImage.getWidth()
    height = anImage.getHeight()
    newImage = EmptyImage(width, height)

    mask = [[1,2,1], [2,1,2], [1,2,1]]

    #convolving and generating new image
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            aPixel = blurConvolve(anImage, r, c, mask)
            newImage.setPixel(c, r, aPixel)
            
    return newImage

def sharpeningImage(anImage):
    width = anImage.getWidth()
    height = anImage.getHeight()
    newImage = EmptyImage(width, height)

    mask = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]

    #convolving and generating new image
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            aPixel = sharpConvolve(anImage, r, c, mask)
            newImage.setPixel(c, r, aPixel)

    return newImage

#enable the function to draw the result of the four digital image processing
def drawTheResult(hfImage, hmImage, blurImage, sharpImage):
    width = hfImage.getWidth()
    height = hfImage.getHeight()
    myWin = ImageWin(width*2, height*2, "Output Image")

    hfImage.draw(myWin)

    hmImage.setPosition(width, 0)
    hmImage.draw(myWin)

    blurImage.setPosition(0, height)
    blurImage.draw(myWin)

    sharpImage.setPosition(width, height)
    sharpImage.draw(myWin)

    myWin.exitOnClick()

fileName = input('Please enter the name of the image : ')
oldImage = FileImage(fileName)
hfImage = horizontalFlip(oldImage)
hmImage = horizontalMirroing(oldImage)
blurImage = blurringImage(oldImage)
sharpImage = sharpeningImage(oldImage)
drawTheResult(hfImage, hmImage, blurImage, sharpImage)
