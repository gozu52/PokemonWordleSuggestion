from asyncio.windows_events import NULL
import pokemonLenFive
import pokemonFirstChoice

# initializing lists
pokeNameInput = []
greenInput = []
yellowInput = []
gList = []
yList = []
listName = pokemonLenFive.ans
suggestList = []
delete_str = []
word_point = []

# making green list
def greenList(i):
    gList = listName
    greenPoint = list(input())
    greenInput.append(greenPoint)

    for j in range(len(greenInput[i])):
        tmp = []
        for k in range(len(listName)):
            if greenInput[i][j] == "1" and pokeNameInput[i][j] == listName[k][j]:
                tmp.append(listName[k])
        if len(tmp) != 0:
            gList = list(set(tmp) & set(gList))
        if len(gList) == len(listName):
            return NULL
    return gList

# making yellow list
def yellowList(i):
    yList = listName
    tmp_yellow = []
    yellowPoint = list(input())
    yellowInput.append(yellowPoint)

    for j in range(len(yellowInput[i])):
        if yellowInput[i][j] == "1":
            tmp_yellow.append(pokeNameInput[i][j])
    for j in range(len(tmp_yellow)):
        tmp = []
        for k in range(len(list(listName))):
            if tmp_yellow[j] in list(listName)[k]:
                tmp.append(list(listName)[k])
        if len(tmp) != 0:
            yList = list(set(tmp) & set(yList))
        if len(yList) == len(listName):
            return NULL
    return yList

# delete Used Words                
def deleteUsedWords(a):
    if not ((a >= 'ｶ' and a<= 'ｺ') and (a >= 'ﾀ' and a<= 'ﾄ') and (a >= 'ﾊ' and a<= 'ﾎ') and (a >= 'ﾔ' and a<= 'ﾖ') and(a >= 'ｱ' and a<= 'ｵ')):
        delete_str.append(a)

# delete List
def deleteList():
    dList = []
    for i in range(len(listName)):
        for j in range(len(delete_str)):
            if not delete_str[j] in listName[i]:
                dList.append(listName[i])
    return dList

# update suggestion list
def updateSuggestList(i):
    if i == 0:
        return suggestList[i]
    else:
        return list(set(suggestList[i]) & set(suggestList[i-1]))

# main process
print("first suggestion:")
firstList = pokemonFirstChoice.ans
print(firstList)

for i in range(10):
    print(i)
    pokeNameInput.append(input())
    gList = greenList(i)
    
    yList = yellowList(i)

    if gList == NULL and yList == NULL:
        currentList = listName
    elif gList == NULL:
        currentList = yList
    elif yList == NULL:
        currentList = gList
    else:
        currentList = list(set(gList) & set(yList))

    word_point.append(list(greenInput[i] or yellowInput[i]))

    for j in range(5):
        if word_point[i][j] == "0":
            deleteUsedWords(pokeNameInput[i][j])

    dList = deleteList()

    listName = list(set(listName) & set(dList))
    
    currentList = list(set(currentList) & set(listName))
    
    suggestList.append(currentList)

    suggestList[i] = updateSuggestList(i)

    print(suggestList[i])