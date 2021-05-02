class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def deQueue(self):
        if len(self.s1)==0:
            print("empty queue")
        else:
            x=self.s1[-1]
            self.s1.pop()
            return x

    def EnQueue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()


Q1=Queue()
Q1.EnQueue(10)
Q1.EnQueue(20)
print(Q1.s1)
Q1.deQueue()
Q1.EnQueue(10)
Q1.EnQueue(20)
print(Q1.s1)
