
def sum_cons(k,A):
    max_sum=0
    for i in range(k):
        max_sum+=A[i]
    window_sum=max_sum
    for i in range(k,len(A)):
        window_sum+=A[i]-A[i-k]
        if(window_sum>max_sum):
            max_sum=window_sum
    return max_sum

a=[1,2,5,3,4]

print(sum_cons(3,a))
