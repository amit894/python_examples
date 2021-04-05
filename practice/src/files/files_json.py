import json

f1 = open("../../resources/sample.json")
j = json.load(f1)
# print(j.keys())
# print(j.values())

for i in j['contents']:
    for k in i['monthlySales']:
        print("%d" %k['month'])
        print("%d" %k['sales'])
