def three_sum(A):
    A.sort()
    indexes=[]
    for i in range(len(A)):
        l=i+1
        r=len(A)-1
        while(l<r):
            if (A[i]+A[l]+A[r]==0):
                if([A[i],A[l],A[r]] not in indexes):
                    indexes.append([A[i],A[l],A[r]])
                l+=1
                r-=1
            elif (A[i]+A[l]+A[r]<0):
                l+=1
            elif (A[i]+A[l]+A[r]>0):
                r=r-1
    return indexes

A=[-2,0,1,1,2]
print(three_sum(A))
