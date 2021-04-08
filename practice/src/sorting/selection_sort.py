def selection_sort(A):
    for i in range(len(A)):
        min_idx=i
        for j in range(i+1,len(A)):
            if A[j]<=A[min_idx]:
                min_idx=j
        A[i],A[min_idx] = A[min_idx],A[i]


A = [56, 21, 21, 32, 43]
selection_sort(A)
print(A)
