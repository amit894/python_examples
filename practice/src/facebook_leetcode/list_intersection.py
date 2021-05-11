def intersect_list(list1,list2):
    intersect_list=[]
    m=len(list1)
    n=len(list2)
    i=j=0
    while i<m and j<n:
        if(max(list1[i][0],list2[j][0])<=min(list1[i][1],list2[j][1])):
            intersect_list.append([max(list1[i][0],list2[j][0]),min(list1[i][1],list2[j][1])])
            if list2[j][1]<list1[i][1]:
                j+=1
            else:
                i+=1
        elif list1[i][0] < list2[j][1]:
            i+=1
        elif list2[j][0] < list1[j][1]:
            j+=1
    return intersect_list

firstList = [[8,15]]
secondList = [[2,6],[8,10],[12,20]]
print(intersect_list(firstList,secondList))
