import csv

# Initializing Dictionary
cntDict = {"ァ":0,"ア":0,"ィ":0,"イ":0,"ゥ":0,"ウ":0,"ェ":0,"エ":0,"ォ":0,"オ":0,
            "カ":0,"ガ":0,"キ":0,"ギ":0,"ク":0,"グ":0,"ケ":0,"ゲ":0,"コ":0,"ゴ":0,
            "サ":0,"ザ":0,"シ":0,"ジ":0,"ス":0,"ズ":0,"セ":0,"ゼ":0,"ソ":0,"ゾ":0,
            "タ":0,"ダ":0,"チ":0,"ヂ":0,"ッ":0,"ツ":0,"ヅ":0,"テ":0,"デ":0,"ト":0,"ド":0,
            "ナ":0,"ニ":0,"ヌ":0,"ネ":0,"ノ":0,
            "ハ":0,"バ":0,"パ":0,"ヒ":0,"ビ":0,"ピ":0,"フ":0,"ブ":0,"プ":0,"ヘ":0,"ベ":0,"ペ":0,"ホ":0,"ボ":0,"ポ":0,
            "マ":0,"ミ":0,"ム":0,"メ":0,"モ":0,
            "ャ":0,"ヤ":0,"ュ":0,"ユ":0,"ョ":0,"ヨ":0,
            "ラ":0,"リ":0,"ル":0,"レ":0,"ロ":0,
            "ワ":0,"ヲ":0,"ン":0,"ー":0}

# Character count
def cntChar(char):
    if char == "ァ":
        cntDict["ァ"] += 1
    elif char == "ア":
        cntDict["ア"] += 1
    elif char == "ィ":
        cntDict["ィ"] += 1
    elif char == "イ":
        cntDict["イ"] += 1
    elif char == "ゥ":
        cntDict["ゥ"] += 1
    elif char == "ウ":
        cntDict["ウ"] += 1
    elif char == "ェ":
        cntDict["ェ"] += 1
    elif char == "エ":
        cntDict["エ"] += 1
    elif char == "ォ":
        cntDict["ォ"] += 1
    elif char == "オ":
        cntDict["オ"] += 1
    elif char == "カ":
        cntDict["カ"] += 1
    elif char == "ガ":
        cntDict["ガ"] += 1
    elif char == "キ":
        cntDict["キ"] += 1
    elif char == "ギ":
        cntDict["ギ"] += 1
    elif char == "ク":
        cntDict["ク"] += 1
    elif char == "グ":
        cntDict["グ"] += 1
    elif char == "ケ":
        cntDict["ケ"] += 1
    elif char == "ゲ":
        cntDict["ゲ"] += 1
    elif char == "コ":
        cntDict["コ"] += 1
    elif char == "ゴ":
        cntDict["ゴ"] += 1
    elif char == "サ":
        cntDict["サ"] += 1
    elif char == "ザ":
        cntDict["ザ"] += 1
    elif char == "シ":
        cntDict["シ"] += 1
    elif char == "ジ":
        cntDict["ジ"] += 1
    elif char == "ス":
        cntDict["ス"] += 1
    elif char == "ズ":
        cntDict["ズ"] += 1
    elif char == "セ":
        cntDict["セ"] += 1
    elif char == "ゼ":
        cntDict["ゼ"] += 1
    elif char == "ソ":
        cntDict["ソ"] += 1
    elif char == "ゾ":
        cntDict["ゾ"] += 1
    elif char == "タ":
        cntDict["タ"] += 1
    elif char == "ダ":
        cntDict["ダ"] += 1
    elif char == "チ":
        cntDict["チ"] += 1
    elif char == "ヂ":
        cntDict["ヂ"] += 1
    elif char == "ッ":
        cntDict["ッ"] += 1
    elif char == "ツ":
        cntDict["ツ"] += 1
    elif char == "ヅ":
        cntDict["ヅ"] += 1
    elif char == "テ":
        cntDict["テ"] += 1
    elif char == "デ":
        cntDict["デ"] += 1
    elif char == "ト":
        cntDict["ト"] += 1
    elif char == "ド":
        cntDict["ド"] += 1
    elif char == "ナ":
        cntDict["ナ"] += 1
    elif char == "ニ":
        cntDict["ニ"] += 1
    elif char == "ヌ":
        cntDict["ヌ"] += 1
    elif char == "ネ":
        cntDict["ネ"] += 1
    elif char == "ノ":
        cntDict["ノ"] += 1
    elif char == "ハ":
        cntDict["ハ"] += 1
    elif char == "バ":
        cntDict["バ"] += 1
    elif char == "パ":
        cntDict["パ"] += 1
    elif char == "ヒ":
        cntDict["ヒ"] += 1
    elif char == "ビ":
        cntDict["ビ"] += 1
    elif char == "ピ":
        cntDict["ピ"] += 1
    elif char == "フ":
        cntDict["フ"] += 1
    elif char == "ブ":
        cntDict["ブ"] += 1
    elif char == "プ":
        cntDict["プ"] += 1
    elif char == "ヘ":
        cntDict["ヘ"] += 1
    elif char == "ベ":
        cntDict["ベ"] += 1
    elif char == "ペ":
        cntDict["ペ"] += 1
    elif char == "ホ":
        cntDict["ホ"] += 1
    elif char == "ボ":
        cntDict["ボ"] += 1
    elif char == "ポ":
        cntDict["ポ"] += 1
    elif char == "マ":
        cntDict["マ"] += 1
    elif char == "ミ":
        cntDict["ミ"] += 1
    elif char == "ム":
        cntDict["ム"] += 1
    elif char == "メ":
        cntDict["メ"] += 1
    elif char == "モ":
        cntDict["モ"] += 1
    elif char == "ャ":
        cntDict["ャ"] += 1
    elif char == "ヤ":
        cntDict["ヤ"] += 1
    elif char == "ュ":
        cntDict["ュ"] += 1
    elif char == "ユ":
        cntDict["ユ"] += 1
    elif char == "ョ":
        cntDict["ョ"] += 1
    elif char == "ヨ":
        cntDict["ヨ"] += 1
    elif char == "ラ":
        cntDict["ラ"] += 1
    elif char == "リ":
        cntDict["リ"] += 1
    elif char == "ル":
        cntDict["ル"] += 1
    elif char == "レ":
        cntDict["レ"] += 1
    elif char == "ロ":
        cntDict["ロ"] += 1
    elif char == "ワ":
        cntDict["ワ"] += 1
    elif char == "ヲ":
        cntDict["ヲ"] += 1
    elif char == "ン":
        cntDict["ン"] += 1
    elif char == "ー":
        cntDict["ー"] += 1

# Reading CSV file
csv_file = open('E:\PokeWordleSuggest\clonePokeWordleSuggest\PokemonWordleSuggestion\src\poke.csv', 'r',encoding="utf-8")
a_list = []
for row in csv.reader(csv_file):
    a_list.append(row[2])
del a_list[0]

# Making pokemon name list
ans_list = []
for i in range(len(a_list)):
    tmp = ""
    for j in range(len(a_list[i])):
        if not (ord(a_list[i][j]) >= 65 and ord(a_list[i][j]) <= 122):
            tmp += a_list[i][j]
    if len(tmp) == 5:
        ans_list.append(tmp)

# Add pokemon which include special characters
ans_list.append("ポリゴン2")
ans_list.append("ポリゴンZ")
ans_list.append("ニドラン♂")
ans_list.append("ニドラン♀")

# Count character execution
for i in range(len(ans_list)):
    for j in range(len(ans_list[i])):
        cntChar(ans_list[i][j])
cntDict = sorted(cntDict.items(), key=lambda x: x[1], reverse=True)

# print(ans_list)
