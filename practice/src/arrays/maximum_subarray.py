def max_subarray(arr):
    max_sum=arr[0]
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        max_sum=max(max_sum,sum)
        if sum<0:
            sum=0
    return max_sum

nums = [5,4,-1,7,8]
print(max_subarray(nums))
