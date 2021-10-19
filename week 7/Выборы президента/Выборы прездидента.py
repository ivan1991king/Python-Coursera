fin = open('input.txt', 'r', encoding='utf-8 sig')
text = []
for line in fin:
    text.append(line.strip())
print(text)
words = {}
for c in text:
    if c not in words:
        words[c]=1
    else:
        words[c] += 1

voices = len(text)
List = sorted(words.items(), key=lambda x: -x[1])
print(List)

percent = List[0][1] / voices * 100
if percent > 50:
    print(List[0][0])
else:
    for name in List[:2]:
        print(name[0])
