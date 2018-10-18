text = str(input()).lower()
text = text.split(' ')
result = {}
key = ""
for word in text:
    if(word not in result):
        result[word] = 1
    else:
        result[word] += 1
for key, value in result.items():
    print(key, value, sep=' ')