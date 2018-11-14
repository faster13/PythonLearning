def uncompress_string(s):
    repeat_d = {}
    curch = ''
    outstr = ""
    for ch in s:
        if(ch not in "0123456789" and len(repeat_d) != 0):
            k, v = repeat_d.popitem()
            outstr += str(k) * int(v)
        if(ch not in "0123456789"):
            curch = ch
            repeat_d[ch] = ""
        if(ch in "0123456789" and len(repeat_d) != 0):
            repeat_d[curch] += ch
    k, v = repeat_d.popitem()
    outstr += str(k) * int(v)
    return outstr

uncode_text = ""         
with open("test.txt") as ofr:
    for line in ofr:
        uncode_text += uncompress_string(line.strip()) + "\n"

with open("uncode.txt", 'w') as ofw:
    ofw.write(uncode_text)
