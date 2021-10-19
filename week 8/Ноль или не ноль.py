print(any(
       map(
               lambda x: int(x) == 0,
               open('input2.txt', 'r', encoding='utf8').read().split()
       )
      )
)