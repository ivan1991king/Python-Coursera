fin = open('input.txt', 'r', encoding='utf-8 sig')
text = []
for line in fin:
    lineList = list(line.strip().split())
    [text.append(c) for c in lineList]

print(text)
words = {}
for c in text:
    if c not in words:
        words[c]=0
    else:
        words[c] += 1
    print(words[c], end = " ")

fin.close()