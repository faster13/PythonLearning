def update_dictionary(d, key, value):
    if(key in d):
        d[key][:] += [value]
    elif(2 * key in d):
        d[2 * key][:] += [value]
    else:
        d[2 * key] = [value]

d = {2:[1]}
update_dictionary(d, 2, -1)
#d[2][:] += [2]
print(d)
