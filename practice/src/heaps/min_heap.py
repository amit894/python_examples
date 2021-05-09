class MinHeap:
    def __init__(self):
        self.heap=[]

    def get_left_child(self,i):
        return (2*i+1)

    def get_right_child(self,i):
        return (2*i+2)

    def get_parent(self,i):
        return (i-1)//2

    def has_left_child(self,i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self,i):
        return self.get_right_child(i) < len(self.heap)

    def has_parent(self,i):
        return self.get_parent(i)>=0

    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def insert(self,key):
        self.heap.append(key)
        if (len(self.heap)>0):
            self.heapify_up(len(self.heap)-1)

    def extract_min(self):
        if (len(self.heap)>0):
            self.heap[0]=self.heap[len(self.heap)-1]
            self.heap.pop()
            self.heapify_down(0)

    def get_min_child_node(self,i):
        if self.has_left_child(i) and self.has_right_child(i):
            if self.heap[self.get_left_child(i)]<=self.heap[self.has_right_child(i)]:
                return self.get_left_child(i)
            else:
                return self.get_right_child(i)
        elif self.has_left_child(i):
            return self.get_left_child(i)
        elif self.has_right_child(i):
            return self.get_right_child(i)
        else:
            return -1

    def heapify_up(self,i):
        while (self.has_parent(i) and self.heap[self.get_parent(i)]>=self.heap[i]):
            self.swap(i,self.get_parent(i))
            i=self.get_parent(i)

    def heapify_down(self,i):
        while ((self.has_left_child(i) or self.has_right_child(i)) and self.heap[i]>=self.heap[self.get_min_child_node(i)]):
            self.swap(i,self.get_min_child_node(i))
            i=self.get_min_child_node(i)



M1=MinHeap()
M1.insert(11)
M1.insert(23)
M1.insert(10)
M1.insert(9)
M1.insert(8)
M1.insert(17)

print(M1.heap)

M1.extract_min()
M1.extract_min()

print("De limiter")

print(M1.heap)

M1.insert(111)
M1.insert(231)
M1.insert(101)
M1.insert(91)
M1.insert(81)

print("De limiter")

print(M1.heap)
