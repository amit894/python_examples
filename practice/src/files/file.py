
f1 = open("../../resources/sample.txt")
print(f1.read()) #Read the whole file
f1.close()

f2 = open("../../resources/sample.txt")
for lines in f2:
    print(lines) #Read the file line by line
f2.close()


f3 = open("../../resources/sample.txt","w")
f3.write("Adding content to the file\n") #write to a file
f3.close()

f3 = open("../../resources/sample.txt","a")
f3.write("Appending content to the file\n") #append to a file
f3.close()
