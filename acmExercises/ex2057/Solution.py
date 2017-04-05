strDict = {}
tmpStr = ""
numOfOp = 0
selectMethod = 0
key = ''

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
            strDict[curVal] = strDict[curVal] + 1
    if selectMethod == 2:
        for key in sorted(strDict):
            print(key)
            break
        if strDict[key] - 1 == 0:
            strDict.pop(key)
        else:
            strDict[key] -= 1
    numOfOp -= 1