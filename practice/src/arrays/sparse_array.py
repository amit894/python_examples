#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    string_count=[]
    for query in queries:
        count=0
        for string in strings:
            if(string==query):
                count+=1
        string_count.append(count)
    return string_count

if __name__ == '__main__':

    strings=[]
    queries=[]

    f1 = open("../../resources/input.txt")
    sizes=f1.readline().split()

    for i in range(int(sizes[0])):
        strings.append(f1.readline().strip())

    for j in range(int(sizes[1])):
        queries.append(f1.readline().strip())

    res = matchingStrings(strings, queries)
    print(res)
