def median(A1,A2):
    M=len(A1)
    N=len(A2)
    md_index=[]
    md_index=median_index(M,N)
    i=0
    j=0
    A3=[]
    while i<M and j<N:
        if A1[i]<=A2[j]:
            A3.append(A1[i])
            i+=1
        else:
            A3.append(A2[j])
            j+=1

    while i<M:
        A3.append(A1[i])
        i+=1

    while j<N:
        A3.append(A2[j])
        j+=1
    sum=0

    for i in range(len(md_index)):
        sum+=A3[md_index[i]]
    return (sum/len(md_index))


def median_index(M,N):
    med_idx=[]
    x=(M+N)//2
    med_idx.append(x)
    if (M+N)%2==0:
        med_idx.append(x-1)
    return med_idx

nums1 = [1,3]
nums2 = [2]

print(median(nums1,nums2))
