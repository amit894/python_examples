import sys
def aVeryBigSum(A,n):
    sum=0
    for i in range(n):
        sum=sum+A[i]
    return sum


A = [10000100, 10000100, 10000100, 10000010]
print(aVeryBigSum(A,len(A)))

B=[]
arr_size=int(input())
for i in range(arr_size):
    B.append(int(input()))

print(aVeryBigSum(B,arr_size))
