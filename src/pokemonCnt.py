import pokemonCsvRead

ans = pokemonCsvRead.ans
cntWord=[0]*46

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] >= 'ｰ' and ans[i][j] <= 'ﾝ':
            cntTmp = ord(ans[i][j])-65392
            cntWord[cntTmp] += 1
# print("cntWord","\n")
print(cntWord)