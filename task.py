def read_file_lines(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        return file.readlines()


a = []

# генератор возвращает значение и запоминает на каком месте исполнения он остановился
# генератор - это итератор(с точки зрения питона)


def read_file_lines2(file_name):  # фабрика генераторов
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            yield f'line from file:{line}'
            print('KEK')


roma_gen = read_file_lines2('roma_kek.js')  # объект-генератор(это и есть генератор)
# print(roma_gen)
# print(roma_gen.__next__())
# print(next(roma_gen))
# print(next(roma_gen))
# print(next(roma_gen))
# .__next__()  - это метод, который попробует вернуть следующее значение из генератора
# next()  - это функция-обертка(по факту, вызывает метод __next__()), то есть пытается вернуть
# следующее значение из генератора.


def by_one(elements):
    for i in elements:
        yield i


names_by_one = by_one(['Dima', 'Irina Batkovna', 'Hleb'])
# print(next(names_by_one))
# print(next(names_by_one))
# print(next(names_by_one))
# print(next(names_by_one, 'Da vse tam bolshe nema nichego'))
# print(next(names_by_one, 'Da vse tam bolshe nema nichego'))
# print(next(names_by_one, 'Da vse tam bolshe nema nichego'))
# когда мы будем пытаться получить значение из пустого генератора, то мы получим
# StopIteration ошибку
# next(gen, default)  - это функция-обертка(по факту, вызывает метод __next__()), то
# есть пытается вернуть следующее значение из генератора(gen). Если будет получена ошибка
# StopIteration, то будет возвращено значение default


# for i in next(names_by_one):  # по генератору можно пройтись циклом
#     print(i)

# next(names_by_one)


# Есть список с именами, у нас есть набор различных ресурсов(функций) которые должны
# обработать каждое из имен. Создать генератор, который будет менять имя на следующее,
# только когда мы в генератор передадим строку 'nextone'. Список имен мы передаем в
# аргумент генератора()


# send(arg)  - отправить значение arg в генератор

def lol():
    for i in range(10):
        data = yield i
        print('1111111>', data)
        if data == 'astanavites':
            break


kek = lol()
# print(kek.send('Hello'))
print(next(kek))
# print(kek.send('Hello'))
# print(kek.send('Hello2'))
# print(kek.send('Hello3'))
# print(kek.send('Hello4'))
# print(kek.send('Hello5'))
# print(next(kek))
# kek.send('Hello')
# print(next(kek))
# print(next(kek))
# kek.send('Hello')
# print(next(kek))


for i in str(kek.send('Hello')):
    print(i)