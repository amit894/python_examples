import re

def ispalindrome(s):
    i=0
    j=len(s)-1
    while(i<=j):
        if (s[i]!=s[j]):
            print("Not a palindrome")
            return
        i+=1
        j-=1
    print("A palindrome")



regex = re.compile('[^a-zA-Z]')
ispalindrome((regex.sub('', 'A man, a plan, a canal: Panama')).lower())
