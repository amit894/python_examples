def merge_intervals(A):
    merge_intervals=[]
    merge_intervals.append(A[0])
    for i in range(1,len(A)):
        if A[i][0]>merge_intervals[len(merge_intervals)-1][1]:
            merge_intervals.append(A[i])
        elif A[i][1]>merge_intervals[len(merge_intervals)-1][1]:
            merge_intervals[len(merge_intervals)-1][1]=A[i][1]
    return merge_intervals

intervals =  [[1,4],[4,5]]
print(merge_intervals(intervals))
