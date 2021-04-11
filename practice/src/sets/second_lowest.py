def second_lowest(list1,set1):
    list2=list(set1)
    students=[]
    list2.sort()
    for i in list1:
        if i[0]==list2[1]:
            students.append(i[1])
    students.sort()
    return students

def print_array(list1):
    for i in list1:
        print(i)

if __name__ == '__main__':
    students =[]
    uniqscores =set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score,name])
        uniqscores.add(score)
    print_array(second_lowest(students,uniqscores))
