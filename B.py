s = "**Hello123**"
a1 = 0
a2 = 0
a3 = 0

for c in s:
    if c.isalpha():
        a1 += 1
    elif c.isdecimal():
        a2 += 1
    else:
        a3 += 1
print(a1)
print(a2)
print(a3)
