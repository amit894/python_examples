def max_sum_subarray(A):
    max_sum=A[0]
    window_sum=max_sum
    for i in range(1,len(A)):
        window_sum = max(A[i], window_sum+A[i])
        max_sum = max(window_sum,max_sum)
    return max_sum


print(max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
