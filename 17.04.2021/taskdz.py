first_number = input('vvedi number-')
second_number = input('vvedi number 2-')
action = input('vvedi action-')
answ = 0
if not isinstance(first_number, int) or not isinstance(second_number, int):
    raise TypeError('first_number or second_number must be integer data type')
if action == '+':
    answ = int(first_number) + int(second_number)
if action == '-':
    answ = int(first_number) - int(second_number)
if action == '*':
    answ = int(first_number) * int(second_number)
if action == '//':
    answ = int(first_number) // int(second_number)
print(answ)