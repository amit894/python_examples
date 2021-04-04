class Node:
	def __init__(self, data):
		self.data=data
		self.next=None


class Queue:

	def __init__(self):
		self.head = None

	def isempty(self):
		if(self.head==None):
			return True

	def size_queue(self):
		if self.isempty():
			return 0
		else:
			element=self.head
			size = 0
			while(element!=None):
				size=size+1
				element=element.next
			return size

	def print_queue(self):
		if self.isempty():
			return 0
		else:
			element=self.head
			while(element!=None):
				print("%d" %element.data)
				element=element.next

	def peek(self):
		if self.isempty():
			print ("Empty Queue nothing to peek")
		else:
			element=self.head
			print ("First element of the Queue is %d" %element.data)

	def push(self,node):
		if self.isempty():
			self.head=node
		else:
		    prev_head=self.head
		    self.head=node
		    node.next=prev_head

	def pop(self):
		if self.isempty():
			print ("Empty Queue nothing to pop")
		else:
			self.head=self.head.next

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
