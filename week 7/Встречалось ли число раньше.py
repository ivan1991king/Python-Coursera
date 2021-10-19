numList = list(map(int, input().split()))
set1 = set()
for num in numList:
    if num in set1:
       print("yes")
    else:
        print('no')
        set1.add(num)

