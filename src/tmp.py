from asyncio.windows_events import NULL
import pokemonCsvRead
pokeNameInput = []
greenInput = []
yellowInput = []
listName = pokemonCsvRead.ans
suggest = []
suggest2 = []
ans = []
delete_str = []
word_point = []


def deleteUsedWords(a):
    if not ((a >= 'ｶ' and a<= 'ｺ') and (a >= 'ﾀ' and a<= 'ﾄ') and (a >= 'ﾊ' and a<= 'ﾎ') and (a >= 'ﾔ' and a<= 'ﾖ') and(a >= 'ｱ' and a<= 'ｵ')):
        delete_str.append(a)

ttt = []

def greenList():
    return NULL

def yellowList():
    return NULL

def deleteList():
    for i in range(len(listName)):
        for j in range(len(delete_str)):
            if not delete_str[j] in listName[i]:
                ttt.append(listName[i])

def suggestList():
    return NULL




for i in range(1):
    
    pokeNameInput.append(input())
    
    greenPoint = list(input())
    greenInput.append(greenPoint)

    yellowPoint = list(input())
    yellowInput.append(yellowPoint)

    word_point = greenPoint or yellowPoint

    for j in range(5):
        if word_point[j] == "0":
            deleteUsedWords(pokeNameInput[i][j])
    
    deleteList()
    listName = set(ttt) ^ set(listName)


    tmp_yellow = []

    for j in range(5):
        if yellowInput[i][j] == "1":
            tmp_yellow.append(pokeNameInput[i][j])

    for j in range(len(tmp_yellow)):
        for k in range(len(list(listName))):
            if tmp_yellow[j] in list(listName)[k]:
                suggest.append(list(listName)[k])

    tmp = []

    
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



print("suggest pokemon list")
if len(suggest2)==0:
    print("Suggestion yellow")
    print(suggest)
else:
    print("Suggestion green")
    print(list(ans))
