x = '1111222211222223'
count_list = []
counter = 0
count_list.append(x)
for i in x:
    if i in count_list:
        counter += 1

print(counter)

