import os
import math

if os.name == "nt":
    from ctypes import windll, c_short, c_char_p, Structure

def moveConsoleCursor(x,y):
    if os.name == "nt":
        STD_OUTPUT_HANDLE = -11
 
        class COORD(Structure):
            pass
        COORD._fields_ = [("X", c_short), ("Y", c_short)]

        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(x, y))
    else:
        print('\033[{};{}H'.format(str(x+1),str(y+1))) 


def calculateVectorLength(pointA, pointB):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    return math.sqrt(x**2+y**2)
