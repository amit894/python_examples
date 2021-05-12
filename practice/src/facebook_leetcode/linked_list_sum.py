class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def linkedlist_to_array(list1,a):
    if list1==None:
        return "Empty list"
    else:
        current_node=list1
        while (current_node):
            a.append(current_node.data)
            current_node=current_node.next
    return a

def array_to_string(arr):
    string=""
    for i in range(len(arr)):
        string+=str(arr.pop())
    return(string.strip())


def sum_linkedlist(list1,list2):
    list1_array=[]
    list2_array=[]
    list1_string=""
    list2_string=""
    linkedlist_to_array(list1,list1_array)
    linkedlist_to_array(list2,list2_array)
    list1_string=array_to_string(list1_array)
    list2_string=array_to_string(list2_array)
    return str(int(list1_string)+int(list2_string))

def insert(list,val):
    if list==None:
        return Node(val)
    else:
        N1=Node(val)
        N1.next=list
        return N1

def string_to_list(string,list):
    for ch in range(len(string)):
        list=insert(list,string[ch])
    return list

def print_list(list):
    if list==None:
        return "Empty list"
    else:
        current_node=list
        while(current_node):
            print(current_node.data)
            current_node=current_node.next


N1=Node(2)
N2=Node(4)
N3=Node(3)
N1.next=N2
N2.next=N3

N4=Node(5)
N5=Node(6)
N6=Node(4)
N4.next=N5
N5.next=N6

L3=None
x=sum_linkedlist(N1,N4)
L3=string_to_list(x,L3)
print_list(L3)
