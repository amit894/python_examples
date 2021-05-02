def icecreamParlor(m, arr):
    indexes={}
    for i in range(len(arr)):
        c=m-arr[i]
        if c in arr:
            if (arr.index(c)!=i):
                if (i+1)<(arr.index(c)+1):
                    indexes[i+1]=arr.index(c)+1
                else:
                    indexes[arr.index(c)+1]=i+1
    indexes=dict_to_list(indexes)
    return indexes

def dict_to_list(d):
    l=[]
    for key in d:
        l.append([key,d[key]])
    return l


m=6
cost=[1, 4, 5, 3, 2]
print(icecreamParlor(m,cost))
