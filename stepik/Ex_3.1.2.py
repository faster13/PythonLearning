def modify_list(l):
    for i in range(0, len(l)):
        if (l[i] % 2 == 0):
            l[i] = int(l[i] / 2)
        else:
            l[i] = 'X'
    while('X' in l):
        l.remove('X')

lst = [1,2,3,5,7]
#print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
