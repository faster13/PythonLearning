def fillDict(dictIn, bitStr):
    words = bitStr.lower().split()
    for word in words:
        if word not in dictIn.keys():
            dictIn[word] = 1
        else:
            dictIn[word] += 1

def maxRepeatInfo(dictIn):
    maxRepeat = max(dictIn.values())
    finalWord = [word for word, freq in dictIn.items() if freq == maxRepeat]
    finalWord.sort()
    #print(finalWord[0])
    res = finalWord[0] + " " + str(maxRepeat)
    return res

dictWords = {}
with open("test.txt") as ofr:
    for line in ofr:
        fillDict(dictWords, line.strip())
print(maxRepeatInfo(dictWords))
