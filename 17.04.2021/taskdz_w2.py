
def canculator(first_number, second_number, action):
    answ= 0
    if not isinstance(first_number, int) or not isinstance(second_number, int):
        raise TypeError('first_number or second_number must be integer data type')
    if action == '+' and action == '-' and action == '*' and action == '//':
        raise ValueError
    if action == '+':
        answ = int(first_number) + int(second_number)
    if action == '-':
        answ = int(first_number) - int(second_number)
    if action == '*':
        answ = int(first_number) * int(second_number)
    if action == '//':
        answ = int(first_number) // int(second_number)
    return answ


print(canculator(123, 123, "+"))

try:
    canculator(123, 123, "+")
    print('No errors')
except (TypeError):
    print('We have error!')
else:
    print('We have no error')

