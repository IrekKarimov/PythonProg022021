"""
Написать программу для сжатия строки, в которой алгоритм работает следующим образом:
 string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1y2a3', то есть последовательность
  одинаковых символов строки заменяется на этот символ и количество его повторений
  в текущей позиции строки.
  xxxxtttсyyaaa -> x4t3с1y2a3
"""

s = "xxxxtttсyyaaa"
s1 = []

for c in s:
    if c not in s1:
        s1.append(c)

ss = ""
for c in s1:
    ss += c + str(s.count(c))

print(ss)
