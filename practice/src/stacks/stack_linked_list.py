class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None


    def is_stack_empty(self):
        if (self.head==None):
            return True
        else:
            return False



    def stack_size(self):
        count=0
        if(self.is_stack_empty()):
            return 0
        else:
            current_node=self.head
            while(current_node!=None):
                count+=1
                current_node=current_node.next
        return count

    def print_stack(self):
        if(self.is_stack_empty()):
            print("Empty Stack")
            return
        else:
            current_node=self.head
            while(current_node!=None):
                print("Data Element %d"%current_node.data)
                current_node=current_node.next

    def peek(self):
        current_node=self.head
        if(self.is_stack_empty()):
            print("Empty Stack")
        else:
            print("Data Element %d" %self.head.data)


    def pop(self):
        current_node=self.head
        if(self.is_stack_empty()):
            print("Empty Stack")
        else:
            self.head=self.head.next


    def push(self,node):
        if(self.is_stack_empty()):
            self.head=node
            return
        else:
            node.next=self.head
            self.head=node


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
S1.print_stack()
print("De limiter")
S1.pop()
print("De limiter")
S1.print_stack()
