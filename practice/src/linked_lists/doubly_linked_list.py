class Node():
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None

class DoublyLinkedList():
	def __init__(self):
		self.head=None

	def count_elements(self):
		length=0
		if (self.head==None):
			print("Number of elements in the DLL is zero")
		else:
			element=self.head
			while(element!=None):
				length=length+1
				element=element.next
		return(length)

	def print_elements(self):
		if (self.head==None):
			print("Number of elements in the DLL is zero")
		else:
			element=self.head
			while(element!=None):
				print("%d" %element.data)
				element=element.next

	def insert_at_head(self,node):
		if(self.head==None):
			self.head=Node
		else:
			self.head.prev=node
			node.next=self.head
			self.head=node
		return

	def insert_after(self,prev_node,node):
		if(self.head==None):
			self.head=Node
		else:
			element=self.head
			while(element!=None):
				if(element==prev_node):
					node.prev=prev_node
					node.next=prev_node.next
					prev_node.next=node
					prev_node.next=node
				element=element.next


N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)
N6=Node(6)
N7=Node(7)
N8=Node(8)
N9=Node(9)
N10=Node(10)
L1=DoublyLinkedList()
L1.head=N1
N1.next=N2
N2.prev=N1
N2.next=N3
N3.prev=N2
N3.next=N4
N4.prev=N3
N4.next=N5
N5.prev=N4
L1.insert_at_head(N6)
L1.insert_after(N1, N9)
L1.insert_after(N9, N10)
L1.insert_after(N4, N7)
L1.insert_after(N3, N8)
L1.print_elements()
