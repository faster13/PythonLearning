strDict = {}
tmpStr = ""
numOfOp = 0
fndKey = [0,0]
sortedFlag = False

f = open("input.txt")

numOfOp = int(f.readline())

while numOfOp > 0:
    tmpStr = f.readline().split()
    selectMethod = int(tmpStr.pop(0))
    if selectMethod == 1:
        curVal = int(tmpStr.pop())
        if curVal not in strDict:
            strDict[curVal] = 1
        else:
            strDict[curVal] += 1
        sortedFlag = True
    if selectMethod == 2:
        if sortedFlag:
            for item in sorted(strDict.items()):
                fndKey = item
                break
            sortedFlag = False
        else:
            fndKey = strDict.
        print(fndKey[0])
        if fndKey[1] > 1:
            strDict[fndKey[0]] -= 1
        else:
            strDict.pop(fndKey[0])
    numOfOp -= 1
