class MaxHeap:
    def __init__(self):
        self.heap=[]

    def get_parent(self,i):
        return (i-1)//2

    def get_left_child(self,i):
        return (2*i+1)

    def get_right_child(self,i):
        return (2*i+2)

    def get_max(self):
        if (len(self.heap)>=0):
            return self.heap[0]

    def has_parent(self,i):
        return self.get_parent(i)>=0

    def has_left_child(self,i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self,i):
        return self.get_right_child(i) < len(self.heap)

    def insert_key(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def extract_max(self):
        if (len(self.heap)>=0):
            root=self.heap[0]
            self.heap[0]=self.heap[len(self.heap)-1]
            self.heap.pop()
            self.heapify_down(0)
            return root
        else:
            return

    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def max_child_index(self,i):
        if (self.has_right_child(i) and self.has_left_child(i)):
            if (self.heap[self.get_right_child(i)]>=self.heap[self.get_left_child(i)]):
                return self.get_right_child(i)
            else:
                return self.get_left_child(i)
        elif (self.has_right_child(i)):
            return self.get_right_child(i)
        elif (self.has_left_child(i)):
            return self.get_left_child(i)
        else:
            return -1


    def heapify_up(self,i):
        while (self.has_parent(i) and self.heap[i]>=self.heap[self.get_parent(i)]):
            self.swap(i,self.get_parent(i))
            i=self.get_parent(i)

    def heapify_down(self,i):
        while (self.heap[i]<self.heap[self.max_child_index(i)]):
            self.swap(i,self.max_child_index(i))
            i=self.max_child_index(i)

    def print_heap(self,i):
        print(self.heap[i],end=" ")
        if (self.has_left_child(i)):
            self.print_heap(self.get_left_child(i))
        if (self.has_right_child(i)):
            self.print_heap(self.get_right_child(i))


MaxH = MaxHeap()
MaxH.insert_key(1)
MaxH.insert_key(3)
MaxH.insert_key(2)
MaxH.insert_key(4)
MaxH.insert_key(5)
MaxH.extract_max()
print("De Limiter")
MaxH.print_heap(0)

MaxH.extract_max()
print("De Limiter")
MaxH.print_heap(0)


MaxH.insert_key(50)
MaxH.insert_key(60)
MaxH.insert_key(70)

print("De Limiter")
print(MaxH.heap)
print("De Limiter")
print(MaxH.print_heap(0))
