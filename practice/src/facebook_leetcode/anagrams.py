MAX=256

def compare(A1,A2):
    for i in range(MAX):
        if A1[i]!=A2[i]:
            return False
    return True

def search(pat,text):
    indexes=[]
    M=len(pat)
    N=len(text)

    pat_zeroes=[0]*MAX
    text_zeroes=[0]*MAX

    for i in range(M):
        pat_zeroes[ord(pat[i])]+=1
        text_zeroes[ord(text[i])]+=1


    for j in range(M,N):
        if (compare(pat_zeroes,text_zeroes)):
            indexes.append(j-M)

        text_zeroes[ord(text[j])]+=1
        text_zeroes[ord(text[j-M])]-=1

    if (compare(pat_zeroes,text_zeroes)):
        indexes.append(M-N)

    return indexes

print(search("abc","cbaebabacd"))
