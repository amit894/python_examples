class Solution:
    def reverse(self, x: int) -> int:
        s=str(abs(x))
        rev_string=""
        for i in range(len(s)-1,-1,-1):
            rev_string+=(s[i])
        if x<=0:
            rev_int=int(rev_string)*-1
        else:
            rev_int=int(rev_string)
        if rev_int>pow(2,31) or rev_int<(pow(-2,31)-1):
            return 0
        else:
            return rev_int
