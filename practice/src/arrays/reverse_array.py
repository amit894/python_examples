def reverse_array(A,n):
    end=len(A)-1
    start=0
    while (start<=end):
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1

A= [1,2,3,4,5,6,7,8,9,10]
reverse_array(A,len(A))
print(A)
