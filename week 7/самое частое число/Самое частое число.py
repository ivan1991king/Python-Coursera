# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:27:58 2017

@author: Maria
"""

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше
# в лексикографическом порядке.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# apple orange banana banana orange
#
# Вывод программы:
# banana
#
# Тест 2
# Входные данные:
# oh you touch my tralala mmm my ding ding dong
#
# Вывод программы:
# ding
#
# Тест 3
# Входные данные:
# q w e r t y u i o p
# a s d f g h j k l
# z x c v b n m
#
# Вывод программы:
# a

fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
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

Max = 0
for key, value in words.items():
    if Max < value:
        Max = value
        print(Max)

for slova in sorted(words.items(), key=lambda x: x[0]):
    if slova[1] == Max:
        print(slova[0], file=fout)
        break

fin.close()
fout.close()
