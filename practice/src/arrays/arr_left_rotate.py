def left_rotate(a,d,n):
	for i in range(d):
		left_rotate_by_one(a,n)

def left_rotate_by_one(a,n):
	temp=a[0]
	for i in range(n-1):
		a[i]=a[i+1] 
	a[n-1]=temp

A = [1,2,3,4]
left_rotate(A,6,4)
print (A)

#Time Complexity : O(d*n)
#Auxililary Space Complexity: O(1)
