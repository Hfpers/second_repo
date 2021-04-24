

def ch(ch_list):
    answ = 0

    for i in ch_list:
        if i % 2 == 0:
            answ = answ
        else:
            i % 2 != 0
            answ = answ + 1
    return answ


print(ch([1, 3, 4]))
