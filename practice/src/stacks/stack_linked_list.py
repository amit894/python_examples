class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None


    def stack_size(self):
        current_node=self.head
        count=0
        if(current_node==None):
            return 0
        else:
            while(current_node!=None):
                count+=1
                current_node=current_node.next
        return count

    def print_stack(self):
        current_node=self.head
        if(current_node==None):
            print("Empty Stack")
            return
        else:
            while(current_node!=None):
                print("Data Element %d"%current_node.data)
                current_node=current_node.next

    def peek(self):
        current_node=self.head
        if(current_node==None):
            print("Empty Stack")
            return
        else:
            while(current_node.next!=None):
                current_node=current_node.next
        print("Data Element %d" %current_node.data)


    def pop(self):
        current_node=self.head
        count=0
        if(current_node==None):
            print("Empty Stack")
            return
        else:
            while(current_node.next!=None):
                temp=current_node
                current_node=current_node.next
            temp.next=None


    def push(self,node):
        current_node=self.head
        if(current_node==None):
            self.head=node
            return
        else:
            while(current_node!=None):
                temp=current_node
                current_node=current_node.next
            temp.next=node


S1=Stack()
print("De limiter")
S1.peek()
S1.pop()
S1.push(Node(2))
print("De limiter")
S1.peek()
S1.push(Node(4))
print("De limiter")
S1.peek()
S1.push(Node(6))
print("De limiter")
S1.peek()
S1.push(Node(8))
print("De limiter")
S1.peek()
S1.push(Node(10))
print("De limiter")
print("De limiter")
S1.peek()
print("De limiter")
S1.print_stack()


S1=Stack()
S1.peek()
S1.pop()
S1.push(Node(2))
S1.push(Node(4))
S1.push(Node(6))
S1.push(Node(8))
S1.peek()
S1.pop()
S1.pop()
S1.peek()
S1.push(Node(4))
S1.push(Node(6))
S1.push(Node(8))
print("De limiter")
S1.print_stack()
