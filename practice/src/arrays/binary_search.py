def binary_search(A,low,high,item):

    if(high>=low):
        mid = (high+low)//2
        if (item>=A[mid]):
            binary_search(A,mid+1,high,item) # Item bigger than the middle condition loop
        else:
            binary_search(A,low,mid-1,item) # Item smaller than the middle condition loop
    else:
        return (-1) # Recurrsion base condition
    return mid


A = [1,2,3,4,5]
n =len(A)
x=binary_search(A,0,n-1,2)
print(x)

#Time Complexity : O(log n)
#Auxililary Space Complexity: O(1)
