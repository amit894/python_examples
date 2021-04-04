class Node():
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList():
	def __init__(self):
		self.head=None

	def print_elements(self):
		if self.head==None:
			print("This is an empty list")
		else:
			element=self.head
			while (element!=None):
				print("%d" %(element.data))
				element=element.next

	def count_elements(self):
		length = 0
		if self.head==None:
			print("This is an empty list")
		else:
			element=self.head
			while (element!=None):
				length=length+1
				element=element.next
		return(length)


N1=Node(1)
N2=Node(2)
N3=Node(3)
L1=LinkedList()
L1.print_elements()
print(L1.count_elements())
L1.head=N1
N1.next=N2
N2.next=N3
L1.print_elements()
print(L1.count_elements())
