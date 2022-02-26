import pokemonFirstChoice
import pokemonList

dictList = pokemonFirstChoice.dictList
ans_list = pokemonList.ans_list
ans_dict = {}
ans = {}

for i in range(len(ans_list)):
    ans_dict[ans_list[i]] = 0

for i in range(len(dictList)):
    ans[dictList[i]] = i
# print(ans)

for i in range(len(ans_list)):
    for j in range(len(ans_list[i])):
        for k in ans.keys():
            if ans_list[i][j] == k:
                ans_dict[ans_list[i]] += ans[k]

ans_dict = dict(sorted(ans_dict.items(), key=lambda x: x[1]))
# print(ans_dict)

# cnt = 0
# for i in ans_dict.keys():
#     print(cnt," ",i)
#     cnt += 1
#     if cnt >= 5:
#         break
    