fin = open('input.txt', 'r', encoding='utf-8')
set1 = set()
for line in fin:
    lineList = set(line.split())
    [set1.add(c) for c in lineList]

print(len(set1))