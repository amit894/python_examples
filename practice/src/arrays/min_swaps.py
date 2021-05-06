def min_swaps(arr,n):
    numberofOnes=0

    for i in range(n):
        if (arr[i]==1):
            numberofOnes+=1

    x=numberofOnes
    max_count_ones=0

    for i in range(x):
        if (arr[i]==1):
            max_count_ones+=1

    window_ones=max_count_ones

    for i in range(x,n):
        if (arr[i]==1 and arr[x-i]==1) or (arr[i]==0 and arr[x-i]==0):
            pass
        if (arr[1]==1 and arr[x-i]==0):
            window_ones+=1
        if (arr[1]==0 and arr[x-i]==1):
            window_ones-=1
        if (window_ones>max_count_ones):
            max_count_ones=window_ones

    return max_count_ones

a = [0, 0, 1, 0, 1, 1, 0, 0, 1]
n = 9
print (min_swaps(a, n))
