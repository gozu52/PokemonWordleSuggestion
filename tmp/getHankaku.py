import csv
import mojimoji

csv_file = open('E:\PokeWordleSuggest\clonePokeWordleSuggest\PokemonWordleSuggestion\src\poke.csv', 'r',encoding="utf-8")

a_list = []
for row in csv.reader(csv_file):
    a_list.append(row[2])
del a_list[0]

ans_list = []

for i in range(len(a_list)):
    tmp = ""
    for j in range(len(a_list[i])):
        if not (ord(a_list[i][j]) >= 65 and ord(a_list[i][j]) <= 122):
            tmp += a_list[i][j]
    if len(tmp) == 5:
        ans_list.append(mojimoji.zen_to_han(tmp))


ans_list.append("ﾎﾟﾘｺﾞﾝ2")
ans_list.append("ﾎﾟﾘｺﾞﾝZ")
ans_list.append("ﾆﾄﾞﾗﾝ♂")
ans_list.append("ﾆﾄﾞﾗﾝ♀")

print(ans_list)
