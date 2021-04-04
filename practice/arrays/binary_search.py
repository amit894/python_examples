def binary_search(A,low,high,item):

    if(high>=low):
        mid = (high+low)//2
        if (item>=A[mid]):
            binary_search(A,mid+1,high,item)
        else:
            binary_search(A,low,mid-1,item)
    else:
        return (-1)
    return mid


A = [1,2,3,4,5]
n =len(A)
x=binary_search(A,0,n-1,2)
print(x)
