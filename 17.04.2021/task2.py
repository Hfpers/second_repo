kek = []
lol = 0
for i in range(2, 10001):
    for j in range(2, i):
        if i % j == 0:
            lol = lol + 1
    if lol == 0:
        kek.append(i)
    else:
        lol = 0
print(kek)