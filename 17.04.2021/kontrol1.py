def kratator(chislo):
    prom = 0
    answ = ''
    for i in chislo:
        if prom % int(i) == 0:
            prom = int(i)
            answ += 'True'
        else:
            answ += 'False'

    return answ


print(kratator('73312'))




