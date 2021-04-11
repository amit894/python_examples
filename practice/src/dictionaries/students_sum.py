def average_marks(list1):
    sum = 0
    for i in range(len(list1)):
        sum=sum+list1[i]
    return(sum/len(list1))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=average_marks(student_marks[query_name])
    print("%.2f" %avg)
