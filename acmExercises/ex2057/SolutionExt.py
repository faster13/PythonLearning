n = input()
set = []
count = 0
boo = True
for i in xrange(n):
    a = raw_input()
    if len(a) > 1:
        if boo == False:
            set = sorted(set, reverse=True)
            for j in xrange(count):
                print (set.pop())
        m, l = a.split()
        set.append(int(l))
        count = 0
        boo = True
    else:
        count += 1
        boo = False
if boo == False:
    set = sorted(set, reverse=True)
    for i in xrange(count):
        print (set.pop())
