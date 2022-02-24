import pokemonCsvRead
pokeNameInput = []
greenInput = []
yellowInput = []
listName = pokemonCsvRead.ans
suggest = []
suggest2 = []
ans = []

for i in range(1):

    pokeNameInput.append(input())

    v_str = list(pokeNameInput[i])

    
    greenPoint = list(input())
    greenInput.append(greenPoint)

    yellowPoint = list(input())
    yellowInput.append(yellowPoint)

    tmp_yellow = []
        
    for j in range(5):
        if yellowInput[i][j] == "1":
            tmp_yellow.append(pokeNameInput[i][j])

    for j in range(len(tmp_yellow)):
        for k in range(len(listName)):
            if tmp_yellow[j] in listName[k]:
                suggest.append(listName[k])
    
    for j in range(len(greenInput[i])):
        t = []
        for k in range(len(suggest)):
            if greenInput[i][j] == "1" and pokeNameInput[i][j] == suggest[k][j]:
                t.append(suggest[k])
        if len(t) != 0:
            suggest2.append(t)

    if len(suggest2) != 0:
        ans = set(suggest2[0])
    for j in range(len(suggest2)):
        ans = set(ans) & set(suggest2[j])

print("suggestion")
if len(suggest2)==0:
    print(suggest)
else:
    print(list(ans))
