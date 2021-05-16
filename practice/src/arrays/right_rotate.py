def right_rotate(A,d,n):
    for i in range(d):
        right_rotate_by_one(A,n)

def right_rotate_by_one(A,n):
    temp=A[n-1]
    for i in range(n-1,0,-1):
        A[i]=A[i-1]
    A[0]=temp

A = [1,2,3,4]
right_rotate(A,2,4)
print (A)
