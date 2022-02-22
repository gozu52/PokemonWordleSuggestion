import csv
import mojimoji

csv_file = open('E:\PokeWordleSuggest\csv\pokemon.csv', 'r',encoding="utf-8")

a_list = []
for row in csv.reader(csv_file):
    a_list.append(row[2])
del a_list[0]

ans = []
cnt =0
cntWord=[0]*46
for i in range(493):
    tmp = ""
    for j in range(len(a_list[i])):
        if a_list[i][j] >= 'ア' and a_list[i][j] <= 'ン' or a_list[i][j] == 'ー':
            tmp += a_list[i][j]
            tmp = mojimoji.zen_to_han(tmp)
    cnt+=1
    if len(tmp) <=5:
        ans.append(tmp)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] >= 'ｰ' and ans[i][j] <= 'ﾝ':
            cntTmp = ord(ans[i][j])-65392
            cntWord[cntTmp] += 1

ans.sort()
