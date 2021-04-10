def liner(line):
    answ = []
    for i in line:
        first = line.find(i)
        second = line.rfind(i)
        answ.append(line[first:second+1:])
    return answ


a = liner('sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae')
print(a)