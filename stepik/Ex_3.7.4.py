f = open("test.txt")
classes_mid_height = {x: "-" for x in range(1, 12)}
classes_people = {x: 0 for x in range(1, 12)}
for line in f.readlines():
    data = list(line.strip().split("\t"))
    data[0] = int(data[0])
    data[2] = float(data[2])
    if classes_mid_height[data[0]] == "-":
        classes_mid_height[data[0]] = data[2]
        classes_people[data[0]] += 1
    else:
        classes_people[data[0]] += 1
        classes_mid_height[data[0]] += data[2]
for k, v in classes_mid_height.items():
    if(v == "-"):
        print(k, v)
    else:
        print(k, (v / classes_people[k]))