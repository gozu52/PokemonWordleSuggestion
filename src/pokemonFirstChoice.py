import pokemonList

# Initializing elements
pokeList = pokemonList.ans_list
dict = dict(pokemonList.cntDict)
dictList = list(dict.keys())
initialSelect = []
# print(dictList)

# List of Pokemon in order of the letters most frequently used.
for i in range(len(dictList)):
    i_l = []
    for i2 in range(len(pokeList)):
        if dictList[i] in pokeList[i2]:
            i_l.append(pokeList[i2])
    if len(i_l) > 0:
        initialSelect.append(i_l)

# A list of things that use a lot of highly used characters
ans = initialSelect[0]
for i in range(len(initialSelect)):
    if len(list(set(ans) & set(initialSelect[i]))) > 0:
        ans = list(set(ans) & set(initialSelect[i]))
    else:
        break
# print(ans)
