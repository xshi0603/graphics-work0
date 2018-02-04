import math
import random

def factorial(x):
    retVal = 1
    if x == 0:
        return retVal
    for x in xrange(1, x):
        retVal *= (x + 1)
    return retVal

def fibb(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else :
        return fibb(x-1) + fibb(x-2)

def rando():
    retVal = random.randint(0, 256)
    return retVal

def modded(x):
    return factorial(x) % 255

def modder(x):
    return x % 255

def createPic(fileName, x, y):
    fh = open(fileName, "w")
    xcounter = x
    ycounter = y
    message = "P3\n"
    message += str(x)
    message += " "
    message += str(y)
    message += "\n"
    message += str(255)
    message += "\n"
    for x in xrange(xcounter):
        for y in xrange(ycounter):
            message += str(rando())
            message += " "    
            message += str(rando())
            message += " "              
            message += str(rando())
            if (y == ycounter - 1):
                message += "\n"    
            else:
                message += "\t"
    #print message
    fh.write(message)
    fh.close()

if __name__ == '__main__':
    createPic("bro.ppm", 500, 500)

