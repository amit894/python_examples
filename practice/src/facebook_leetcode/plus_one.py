def plus_one(A):
    sum=0
    result=[]
    for i in range(len(A)):
        sum+=pow(10,len(A)-i-1)*A[i]
    for j in (str(sum+1)):
        result.append(j)
    return result

A=[1,2,4]
print(plus_one(A))
