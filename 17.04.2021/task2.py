

def count(twoj_list):
    count_list = []
    counter = 0
    for i in twoj_list:
        if i not in count_list:
            count_list.append(i)

    for j in twoj_list:
        if j in count_list:
            counter += 1
    print(j)
    return counter

print(count('1111222211222223'))
