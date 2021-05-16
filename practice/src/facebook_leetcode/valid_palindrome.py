def isValidPalindrome(string):
    i=0
    j=len(string)-1
    while (i<=j):
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True

def isValidPalindromeOneDigit(string):
    i=0
    j=len(string)-1
    while (i<=j):
        if string[i]==string[j]:
            i+=1
            j-=1
        if isValidPalindrome(string[i:j]):
            return True
        if isValidPalindrome(string[i+1:j+1]):
            return True
        else:
            return False
    return True



print(isValidPalindromeOneDigit("abac"))
