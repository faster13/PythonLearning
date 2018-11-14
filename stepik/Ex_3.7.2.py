def codePhrase(phrase, dict, direction = "from"):
    outStr = ""
    for ch in phrase:
        if(direction == "to"):
            for k, v in dict.items():
                if(ch == k):
                    outStr += v
        if(direction == "from"):
            for k, v in dict.items():
                if(ch == v):
                    outStr += k
    return outStr

c = 4
inpArr = ["dcba", "badc", "dcba", "badc"]
#inpArr = []
#while c > 0:
#    inpArr.append(str(input()).strip())
#    c -= 1
#oneKey = list(str(input()).strip())
#towKey = list(str(input()).strip())
#onePhrase = list(str(input()).strip())
#towPhrase = list(str(input()).strip())
sypherDict = {a: b for a, b in zip(list(inpArr[0]), list(inpArr[1]))}
result = codePhrase(inpArr[2], sypherDict, "to")
print(result)
result = codePhrase(inpArr[3], sypherDict, "from")
print(result)