s = "xxxxtttсyyaaa"
s1 = []

for c in s:
    if c not in s1:
        s1.append(c)

ss = ""
for c in s1:
    ss += c + str(s.count(c))

print(ss)
