def f(x):
    print("OK")
    return 10

result = {}
outStr = ""
for step in range(0, int(input())):
    num = int(input())
    if(num not in result):
        result[num] = f(num)
        outStr += str(result[num]) + "\n"
    else:
        outStr += str(result[num]) + "\n"
print(outStr)
