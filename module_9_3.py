first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(second_result))
# Здесь len(first) = 3, так как в списке всего 3 элемента.
# Указав, по сути, тройку внутри функции range, мы выводим элементы с индексом от 0 до 2
# (так как range выводит последовательность, не включая указанное в скобках число).
# В целом, можно было взять и len(second) - там тоже ровно 3 элемента
