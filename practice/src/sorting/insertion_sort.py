def insertion_sort(A):
    for i in range(len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j]=A[j+1]
            j=j-1
        A[j+1]=key

A = [56, 21, 21, 32, 43]
insertion_sort(A)
print(A)

#Time Complexity: O(n^2)
#Auxiliary Space: O(1)
#Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
