def icecreamParlor(m, arr):
    ice_cream={}
    for i in range(len(cost)):
        diff=m-cost[i]
        if diff in cost:
            if (i<cost.index(diff)):
                ice_cream[i+1]=cost.index(diff)+1
            elif (i>cost.index(diff)):
                ice_cream[cost.index(diff)+1]=i+1
    ice_cream=dict_to_list(ice_cream)
    return ice_cream

def dict_to_list(d):
    l=[]
    for key in d:
        l.append([key,d[key]])
    return l


m=6
cost=[1, 4, 5, 3, 2]
print(icecreamParlor(m,cost))
