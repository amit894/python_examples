import csv

f1 = open("../../resources/sample.csv")
csv_reader= csv.reader(f1, delimiter=',')
for row in csv_reader:
    print(row[0])
