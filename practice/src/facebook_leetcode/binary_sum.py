class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=bin(int(a,2)+int(b,2))
        print(s[2:])

S1=Solution()
S1.addBinary("10","10")
