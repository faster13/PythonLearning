import requests

def sum(a, b):
    a[0] = a[0] + b

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/373.txt')
count = [0]
[sum(count, 1) for str in r.text.strip().splitlines()]
print(count[0])
