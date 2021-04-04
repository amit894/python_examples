class Node:
	def __init__(self, data):
		self.data=data
		self.next=None


class Stack:

	def __init__(self):
		self.head = None

	def isempty(self):
		if(self.head==None):
			return True

	def size_stack(self):
		if self.isempty():
			return 0
		else:
			element=self.head
			size = 0
			while(element!=None):
				size=size+1
				element=element.next
			return size

	def print_stack(self):
		if self.isempty():
			return 0
		else:
			element=self.head
			while(element!=None):
				print("%d" %element.data)
				element=element.next

	def peek(self):
		if self.isempty():
			print ("Empty stack nothing to peek")
		else:
			element=self.head
			while(element.next!=None):
				element=element.next
			print ("Last element of the stack is %d" %element.data)

	def push(self,node):
		if self.isempty():
			self.head=node
		else:
			element=self.head
			while(element.next!=None):
				element=element.next
			element.next=node

	def pop(self):
		if self.isempty():
			print ("Empty stack nothing to pop")
		else:
			element=self.head
			while(element.next!=None):
				 prev=element
				 element=element.next
			prev.next=None

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
