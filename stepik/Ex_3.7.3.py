cnt_gramar_words = int(input())
gramar_words = []
while cnt_gramar_words > 0:
    gramar_words.append(str(input()).strip().lower())
    cnt_gramar_words -= 1
cnt_text_lines = int(input())
text_lines = []
while cnt_text_lines > 0:
    text_lines.append(str(input()).strip().lower())
    cnt_text_lines -= 1
bad_words = set()
for text_line in text_lines:
    for word in text_line.split(" "):
        if word not in gramar_words:
            bad_words.add(word)
for word in bad_words:
    print(word)
