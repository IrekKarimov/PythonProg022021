s = "кот арбуз слово завтрак кнопка лес Лоб"
s = s.split()
n = "45"

btn = {"1": ".,-",
       "2": "абвг",
       "3": "дежз",
       "4": "ийкл",
       "5": "мноп",
       "6": "рсту",
       "7": "фхцч",
       "8": "шщъы",
       "9": "ьэюя",
       "0": "xt9"}

b = []

for c in s:
    s1 = c.lower()
    s1 = s1[0]
    for x in n:
        if s1 in btn[x]:
            b.append(c)
print(*b)

