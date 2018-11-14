def matrix_print(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i]) - 1):
            print(str(m[i][j]) + ' ', end = '')
        print(str(m[i][len(mas[i]) - 1]))

#main code
n = int(input()) 
count = 1
m = [[0 for j in range(n)] for i in range(n)]
c = 0
while(count <= n * n):
    # 1 right
    for i in range(c, n - c):
        m[c][i] = count
        count += 1
    # 2 down
    for i in range(c + 1, n - c):
        m[i][(n - 1) - c] = count
        count += 1
    # 3 left
    for i in range((n - 2) - c, c - 1, -1):
        m[(n - 1) - c][i] = count
        count += 1
    # 4 up
    for i in range((n - 2) - c, c, -1):
        m[i][c] = count
        count += 1
    c += 1
matrix_print(m)
