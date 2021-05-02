#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    sides=[]
    for letter in word:
        sides.append(h[ord(letter)-97])
    sides.sort()
    return(sides[len(sides)-1]*len(sides))

if __name__ == '__main__':

    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5 ,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    word = "abc"
    result = designerPdfViewer(h, word)
    print(result)
