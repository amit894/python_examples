def mergeSort(A):
    if len(A)>1:
        mid=len(A)//2
        L=A[:mid]
        R=A[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i<len(L) and j<len(R) and k<len(A):
            if L[i]<R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            A[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            A[k]=R[j]
            j+=1
            k+=1

A = [56, 21, 21, 32, 43]
mergeSort(A)
print(A)


#Time Complexity: Sorting Aays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
#T(n) = 2T(n/2) + θ(n)
#O(n*log n)

#The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of Master Method and the solution of the recurrence is θ(nLogn). Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the Aay into two halves and takes linear time to merge two halves.
#Auxiliary Space: O(n)
#Algorithmic Paradigm: Divide and Conquer
#Sorting In Place: No in a typical implementation
#Stable: Yes
