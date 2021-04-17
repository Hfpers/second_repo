first_number = input('vvedi number-')
second_number = input('vvedi number 2-')
action = input('vvedi action-')
answ = 0
if action == '+':
    answ = int(first_number) + int(second_number)
if action == '-':
    answ = int(first_number) - int(second_number)
if action == '*':
    answ = int(first_number) * int(second_number)
if action == '//':
    answ = int(first_number) // int(second_number)
print(answ)

try:
    if not isinstance(first_number, int) or not isinstance(second_number, int):
        print('No errors')
except (TypeError):
    print('We have error!')
else:
    print('We have no error')
finally:
    print('I do not care about errors')