def bank(day, procent, deneg):
    pribul = 0
    ch = 0
    while ch < day:
        pribul = float(deneg * procent / 100)
        pribul = float(pribul / 365)
        pribul = float(pribul * day)
        deneg += pribul
        pribul == deneg
        ch += 1
        print(ch)
    return deneg


print(bank(2, 15, 100))
