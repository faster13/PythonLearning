import requests

link = "https://stepic.org/media/attachments/course67/3.6.3/"
fname = "699991.txt"

while "We" not in fname:
    r = requests.get(link + fname)
    fname = r.text.strip()
    print(fname)
r = requests.get(link + fname)
print(r.text.splitlines())