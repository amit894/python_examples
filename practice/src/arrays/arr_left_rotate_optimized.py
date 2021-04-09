def gcd(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    else:
        return gcd(b, a%b)

def print_array(A,n):
    for i in range(n):
        print( "Array Elemement %d" %A[i])

def left_rotate(A,d,n):
    d=d%n
    g_c_d = gcd(d,n)

    for i in range(g_c_d):
        temp = A[i]
        j=i
        while 1:
            k=j+d
            if k>=n: #Diving K by N, so that no array bound of exception
                k=k-n
            if k==i: # The first set getting repeated condition
                break
            A[j]=A[k]
            j=k
        A[j]=temp

A = [1,2,3,4]
left_rotate(A,6,4)
print (A)

#Time Complexity : O(n)
#Auxililary Space Complexity: O(1)
