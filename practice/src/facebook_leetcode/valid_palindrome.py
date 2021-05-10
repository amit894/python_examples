class Solution:
    def isValidPalindrome(self,a,low,high):
        while (low<=high):
            if a[low]!=a[high]:
                return False
            low+=1
            high-=1
        return True


    def validPalindrome(self,a):
        low=0
        high=len(a)-1
        while(low<=high):
            print(a[low],a[high])
            if (a[low]==a[high]):
                low+=1
                high-=1
            else:
                if (self.isValidPalindrome(a,low+1,high)):
                    return True
                if (self.isValidPalindrome(a,low,high-1)):
                    return True
                return False
        return True

S=Solution()
result=S.validPalindrome("atbbga")
print(result)
