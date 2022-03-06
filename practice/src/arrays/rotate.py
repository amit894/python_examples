
class Rotate():
    def __init__(self,arr,rotations,len):
        self.arr=arr
        self.rotations=rotations
        self.len=len


    def left_rotate_by_one(self):
        temp=self.arr[0]
        for i in range(self.len-1):
            self.arr[i]=self.arr[i+1]
        self.arr[self.len-1]=temp

    def right_rotate(self):
        for i in range(self.rotations):
            self.right_rotate_by_one()



    def left_rotate(self):
        for i in range(self.rotations):
            self.left_rotate_by_one()


    def right_rotate_by_one(self):
        temp=self.arr[self.len-1]
        for i in range(self.len-1,-1,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[0]=temp


A=[1,2,3,4,5]
R1=Rotate(A,1,5)
R1.left_rotate()
print(A)
R1.right_rotate()
print(A)
