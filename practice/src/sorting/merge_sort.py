def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i<len(L) and j<len(L):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

A = [56, 21, 21, 32, 43]
mergeSort(A)
print(A)


#Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
#T(n) = 2T(n/2) + θ(n)

#The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of Master Method and the solution of the recurrence is θ(nLogn). Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
#Auxiliary Space: O(n)
#Algorithmic Paradigm: Divide and Conquer
#Sorting In Place: No in a typical implementation
#Stable: Yes
