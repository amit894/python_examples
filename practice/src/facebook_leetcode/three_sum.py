def three_sum(A):
    A.sort()
    print(A)
    indexes=[]
    for i in range(len(A)-2):
        l=i+1
        r=len(A)-1
        while(l<=r):
            if (A[i]+A[l]+A[r]==0) and (l!=r and i!=l and r!=i):
                indexes.append([A[i],A[l],A[r]])
                break
            elif A[i]+A[l]+A[r]<0:
                l+=1
            else:
                r-=1
    return indexes

A=[-1,0,1,2,-1,-4]
print(three_sum(A))
