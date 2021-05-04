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
