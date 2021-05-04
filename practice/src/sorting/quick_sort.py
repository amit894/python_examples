def partition(arr, low, high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return(i+1)

def quick_sort(arr,low,high):
    if len(arr)==1:
        return arr
    elif low <=high:
        pi=partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

A = [56, 21, 21, 32, 43]
quick_sort(A,0,len(A)-1)
print(A)


# Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.
#
#  T(n) = T(0) + T(n-1) + \theta(n)
# which is equivalent to
# T(n) = T(n-1) + \theta(n)
# The solution of above recurrence is  \theta(n2).


# Best Case: The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case. 
#
#  T(n) = 2T(n/2) + \theta(n)
# The solution of above recurrence is \theta        (nLogn). It can be solved using case 2 of Master Theorem.
#
# Average Case:
# To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy.
# We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.
#
#  T(n) = T(n/9) + T(9n/10) + \theta(n)
# Solution of above recurrence is also O(nLogn)
