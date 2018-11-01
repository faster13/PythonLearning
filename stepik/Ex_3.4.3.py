def fillSet(desciples, bitStr):
    words = bitStr.split(';')
    print((int(words[1]) + int(words[2]) + int(words[3])) / 3)
    desciples.append([int(words[1]), int(words[2]), int(words[3])])
    
def middleScore(desciples):
    totalMath = 0
    totalPhys = 0
    totalRus = 0
    for item in desciples:
        totalMath += item[0]
        totalPhys += item[1]
        totalRus += item[2]
    print(str(totalMath / len(desciples)), str(totalPhys / len(desciples)), str(totalRus / len(desciples)), sep=' ')

wordsSet = list()
with open("test.txt") as ofr:
    for line in ofr:
        fillSet(wordsSet, line.strip())
middleScore(wordsSet)