class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def deQueue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("Empty Queue")
        else:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
            x=self.s2.pop()
            while len(self.s2)!=0:
                self.s1.append(self.s2.pop())
            return x


    def EnQueue(self,x):
        self.s1.append(x)


Q1=Queue()
Q1.EnQueue(10)
Q1.EnQueue(20)
print(Q1.s1)
print(Q1.deQueue())
Q1.EnQueue(10)
Q1.EnQueue(20)
print(Q1.s1)
