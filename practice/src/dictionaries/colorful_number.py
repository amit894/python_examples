def is_colorful(s):
    product_set=[]
    for i in s:
        k=(product(i))
        if k in product_set:
            return ("Not match")
        else:
            product_set.append(k)
    return product_set

def product(string):
    product=1
    for i in string:
        product=product*int(i)
    return product

def subString(s, n):
    ss=[]
    for i in range(n):
        for len in range(i+1,n+1):
            ss.append(s[i: len])
    return ss

# Driver program to test above function
s = "327";
s1=subString(s,len(s))
print(is_colorful(s1))
