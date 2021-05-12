def rangeSum(A,m,n):
    left_window_sum=0
    right_window_sum=0

    for j in range(m):
        left_window_sum+=A[j]

    for j in range(n):
        right_window_sum+=A[j]

    return (right_window_sum-left_window_sum)

A=[1,2,3,4]
print(rangeSum(A,0,2))
