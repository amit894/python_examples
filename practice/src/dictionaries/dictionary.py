D1 = {}
print(len(D1)) #Returns the size of the dictionary

D1['Amit']=50 #adding an element to dictionary
print(len(D1))

print(D1['Amit']) # access an element in an dictionary

D2={"key1":"value1","key2":"value2","key3":"value3","key4":"value4","key5":"value5","key6":"value6" }
print(len(D2)) #Returns the size of the dictionary

D2.pop("key1")
print(len(D2)) #Deletes an key from dictionary
print(D2)

D2.popitem() #Deletes an aribtory item from dictionary
print(len(D2))
print(D2)

D2.clear() #Deletes all items from dictionary
print(len(D2))
print(D2)

D3={"key1":"value1","key2":"value2","key3":"value3","key4":"value4","key5":"value5","key6":"value6" }
for key in D3:
    print(D3[key]) #accesing Elements using key

for key,value in D3.items():
    print(value) #accesing Elements using value
