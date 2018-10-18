def f(x):
    return 10

ans={}
for x in range(int(input())):
    t=int(input())
    if t not in ans: ans[t]=f(t)
    print(ans[t])