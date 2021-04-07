import sys
import re


# ^ Begins with in Regex
# $ Ends with in Regex
# * Zero or more occurences
# + One or more occurences
# {} exact number of occurences

for lines in sys.stdin: #Seaching for character in Stdin
    print(lines)
    m = re.search('x',lines)
    try:
        m.group(0)
    except (TypeError,AttributeError):
        print("Match Not found")

for lines in sys.stdin:
    print(lines)
    m = re.split('x',lines) #Splitting by character in Stdin
    try:
        print(m)
    except (TypeError,AttributeError):
        print("Match Not found")

for lines in sys.stdin: #Seaching for starts with in Stdin
    print(lines)
    m = re.search('^Amit',lines)
    try:
        m.group(0)
    except (TypeError,AttributeError):
        print("Match Not found")

for lines in sys.stdin: #Splits for any occurence of a lower alphabet
    print(lines)
    m = re.split('[a-z]',lines)
    try:
        print(m)
    except (TypeError,AttributeError):
        print("Match Not found")

for lines in sys.stdin: #Splits for any occurence of a set of alphabets
    print(lines)
    m = re.split('[a-z]*',lines)
    try:
        print(m)
    except (TypeError,AttributeError):
        print("Match Not found")
