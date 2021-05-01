class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.rear=None

    def is_stack_empty(self):
        if (self.head==None):
            return True
        else:
            return False

    def queue_size(self):
        count=0
        if(self.is_stack_empty()):
            return 0
        else:
            current_node=self.head
            while(current_node!=None):
                count+=1
                current_node=current_node.next
        return count

    def print_queue(self):
        if(self.is_stack_empty()):
            print ("No elements in the queue")
        else:
            current_node=self.head
            while(current_node!=None):
                print ("Data is %d" %current_node.data)
                current_node=current_node.next


    def EnQueue(self,node):
        if(self.is_stack_empty()):
            self.head=self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def DeQueue(self):
        if(self.is_stack_empty()):
            print ("No elements in the queue")
        else:
            self.head=self.head.next
            if(self.head==None):
                self.rear=None

Q1=Queue()
Q1.DeQueue()
Q1.EnQueue(Node(2))
Q1.EnQueue(Node(4))
Q1.EnQueue(Node(6))
Q1.EnQueue(Node(8))
print("De limiter")
Q1.print_queue()
Q1.DeQueue()
print("De limiter")
Q1.print_queue()
