L = ['1','2','3','4']
print(''.join(L))  #List to String Conversion

L = []
print("List Elements",L)
print("Length of List is %d" %len(L)) #Printing an Empty List

L.append(1)
print("List Elements",L)
print("Length of List is %d" %len(L)) # Appending an element to end of list


L.append(1)
L.append(2)
L.append(3)
L.append(4)
print("List Elements",L)
print("Length of List is %d" %len(L)) # Appending an element to end of list

L.insert(2,12)
print("List Elements",L)
print("Length of List is %d" %len(L)) # Inserting an element in middle of list

print(L.index(3)) #Prining the index of an elment in list

L.pop(1)
print("List Elements",L)
print("Length of List is %d" %len(L))

L.sort()
print("List Elements",L #Ascending order

L.reverse()
print("List Elements",L) #Descending order
