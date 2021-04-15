class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None

    def queue_size(self):
        count=0
        current_node=self.head
        if(current_node==None):
            return 0
        else:
            while(current_node!=None):
                count+=1
                current_node=current_node.next
        return count

    def print_queue(self):
        current_node=self.head
        if(current_node==None):
            print ("No elements in the queue")
        else:
            while(current_node!=None):
                print ("Data is %d" %current_node.data)
                current_node=current_node.next

    def peek(self):
        if(self.head==None):
            print ("No elements in the queue nothing to peek")
        else:
            print ("Data is %d" %self.head.data)


    def pop(self):
        if(self.head==None):
            print ("No elements in the queue nothing to pop")
        else:
            self.head=self.head.next

    def push(self,node):
        if(self.head!=None):
            node.next=self.head
        self.head=node

Q1=Queue()
Q1.peek()
Q1.pop()
Q1.push(Node(2))
Q1.push(Node(4))
Q1.push(Node(6))
Q1.push(Node(8))
Q1.peek()
Q1.pop()
Q1.pop()
Q1.peek()
Q1.push(Node(4))
Q1.push(Node(6))
Q1.push(Node(8))
print("De limiter")
Q1.print_queue()
