import pokemonCsvRead

tmp = pokemonCsvRead.ans
ans = []
for i in range(len(tmp)):
    if len(tmp[i])==5:
        ans.append(tmp[i])
# print(ans)
