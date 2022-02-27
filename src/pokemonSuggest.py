import pokemonList
import pokemonValueWeighting

# Initialize the list
pokeList = pokemonList.ans_list
yList = pokemonList.ans_list
gList = pokemonList.ans_list
cntDict = dict(pokemonList.cntDict)
weightingList = pokemonValueWeighting.ans_dict
ansSuggest = []
firstVal = []

# First suggestion
print("first suggestion:")
weightingList = pokemonValueWeighting.ans_dict
cnt = 0
for i in weightingList.keys():
    print(i," ",weightingList[i])
    cnt += 1
    if cnt >= 5:
        break
print()

# main process
for i in range(10):
    print(i+1,"回目")

    # Input each element
    pokeName = input("Enter full-width katakana: ")
    greenP = list(input("Enter green points: "))
    yellowP = list(input("Enter yellow points: "))
    
    # Logical sum
    zeroP = [max(t) for t in zip(greenP, yellowP)]

    # Complete pattern
    cntCmp = 0
    for j in range(len(zeroP)):
        if zeroP[j] == "1":
            cntCmp += 1
    if cntCmp == 5:
        print()
        print(i+1,"回目 ")
        print("Today's answer is: ",pokeName)
        print()
        break
    
    # Create each list
    for j in range(len(zeroP)):
        # Initialize tmp list
        zeroTmp = []
        yellowTmp = []
        greenTmp = []
        for k in range(len(pokeList)):
            if zeroP[j] == "0" and not pokeName[j] in pokeList[k]:
                zeroTmp.append(pokeList[k])
            if zeroP[j] == "1" and pokeName[j] in pokeList[k]:
                yellowTmp.append(pokeList[k])
            if greenP[j] == "1" and pokeName[j] == pokeList[k][j]:
                greenTmp.append(pokeList[k])
        if len(zeroTmp) > 0:
            pokeList = list(set(zeroTmp) & set(pokeList))
        if len(yellowTmp) > 0:
            yList = list(set(yellowTmp) & set(yList))
        if len(greenTmp) > 0:
            gList = list(set(greenTmp) & set(gList))
    
    # Integerate each list
    if not len(gList)==0 and not len(yList)==0:
        pokeList = list(set(pokeList) & set(yList) & set(gList))

    # Create a weighted list of suggestions
    cnt = 0
    ans = []
    value = []
    for j in weightingList.keys():
        for k in range(len(pokeList)):
            if pokeList[k] == j:
                if cnt >= 5:
                    break
                tmp = pokeList[k]+"  value: "+str(weightingList[pokeList[k]])
                ans.append(tmp)
                cnt += 1
    ansSuggest.append(ans)

    # print ansList
    for j in range(len(ans)):
        print(j+1," ",ans[j])
    print()
    