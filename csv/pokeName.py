import csv
#import pandas as pd

csv_file = open('pokemon.csv', 'r',encoding="utf-8")
# f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# header = next(f)
# print(header)
# for row in f:
#     print(row)

a_list = []
for row in csv.reader(csv_file):
    a_list.append(row[2])
del a_list[0]
#print(a_list)

ans = []
print(ans)
#print(len(a_list))
cnt =0

for i in range(493):
    tmp = ""
    for j in range(len(a_list[i])):
        if a_list[i][j] >= 'ア' and a_list[i][j] <= 'ン' or a_list[i][j] == 'ー':
            #a_list[i] = a_list[i].replace(' ', '_')
            #print(a_list[i][j])
            tmp += a_list[i][j]
    #print(tmp)
    cnt+=1
    if len(tmp) <=5:
        ans.append(tmp)

#print(cnt)
#print(a_list)
print(ans)
# tmp = pd.read_csv('pokemon.csv')
# print(tmp)