"""
Большинство сайтов предоставляет возможность оставить комментарий, поэтому необходимо вести их учет,
 иногда можно увидеть такую запись:
Комментарии (28)
Давайте составим программу, которая будет записывать слово "комментарий" в нужной форме, например:
24 комментария
"""

n = "12"
if len(n) > 1:
    n = n[-2]
else:
    n = n[-1]

s = "комментар"

if n == "1":
    s += "ий"
elif n in ["2", "4"]:
    s += "ия"
else:
    s += "иев"
print(n)
