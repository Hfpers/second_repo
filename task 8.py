a = int(input('-'))
b = 0
ch = 0
while a >= 1:
    if a % 2 == 0:
        break
    else:
        b = a % 2
        ch += 1

print(ch)