def minswaps(arr):
    count=0
    unplaced_zeroes=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==0:
            unplaced_zeroes+=1
        else:
            count+=unplaced_zeroes
    return count

arr = [0, 0, 1, 0, 1, 0, 1, 1]
print(minswaps(arr))
