S = input()
pos1 = S.find('f')
print(pos1)
if pos1 != -1:
    print(pos1, end=' ')
pos2 = S.rfind('f')
if pos2 != pos1:
    print(pos2)
if pos1 == -1 and pos2 == -1:
    print('')
