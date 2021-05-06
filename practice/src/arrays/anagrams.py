def anagram_positions(s,p):
    s1=[]
    n=len(p)
    for i in range(len(s)):
        if sorted(s[i:i+n])==sorted(p):
            s1.append(i)
    return s1

s="abab"
p="ab"
print(anagram_positions(s,p))
