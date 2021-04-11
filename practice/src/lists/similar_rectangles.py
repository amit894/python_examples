#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nearlySimilarRectangles' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
#

def nearlySimilarRectangles(sides):
    rect_count=0
    sides.sort()
    for i in range(len(sides)):
        if((sides[i][0] or sides[i][1])==0):
            break
        for j in range(i+1,len(sides)):
            if((sides[j][0] or sides[j][1])==0):
                break
            if(sides[i][0]/sides[j][0]==sides[i][1]/sides[j][1]):
                rect_count=rect_count+1
    return rect_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
