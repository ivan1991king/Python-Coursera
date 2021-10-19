fin = open('input.txt', 'r', encoding = 'utf-8-sig')
fout = open('output.txt', 'w', encoding = 'utf-8')

Array  = []
for line in fin:
    Array.append(line)
print(Array)
Array.sort()
print(Array)

for i in range(0, len(Array)):
    Pos1 = Array[i].find(" ")
    fam = Array[i][0:Pos1].strip()

    Pos2 = Pos1 + Array[i][Pos1+1:].find(' ')
    name = Array[i][Pos1+1:Pos2+1]

    Pos3 = Array[i].rfind(' ')
    bal = Array[i][Pos3:].strip()

    print(fam, name, bal, file = fout)
fin.close()
fout.close()
