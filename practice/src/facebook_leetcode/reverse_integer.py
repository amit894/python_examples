def integer_to_array(integer):
    arr=[]
    string=str(abs(integer))
    i=len(string)-1
    while i>=0:
        arr.append(int(string[i]))
        i-=1
    return arr

def array_to_string(array):
    string=""
    for i in array:
        string+=str(i)
    return int(string)

def reverse_digits(integer):
    string=integer_to_array(integer)
    i1=array_to_string(string)
    y=pow(2,31)-1
    if i1>y:
        return 0
    if integer<=0:
        i1=i1*-1
    return i1

print(reverse_digits(-123))
