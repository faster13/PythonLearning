def f(x):
    result = None
    if(x <= -2):
        result = 1 - (x + 2) ** 2
    if(-2 < x and x <= 2):
        result = -(x / 2.0)
    if(2 < x):
        result = (x - 2) ** 2 + 1
    return result

print(f(1))