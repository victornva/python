'''6. Реализовать два небольших скрипта:
   а) итератор, генерирующий целые числа, начиная с указанного,
   б) итератор, повторяющий элементы некоторого списка, определенного заранее.
   Подсказка: использовать функцию count() и cycle() модуля itertools.
   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
   Необходимо предусмотреть условие его завершения.
   Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
print("\nУрок 4 задание 6\nФормат строки запуска: python task_4_6.py <начальное число> <конечное число>\nПример: python task_4_6.py 5 10 3\n")
'''
Формат строки запуска: python task_4_6.py <начальное число> <конечное число> <число итераций>
Пример: python task_4_6.py 5 10 3
'''
from sys import argv
from itertools import count, cycle

script_name, first_num, last_num, iter_num = argv
my_list = []

for el in count(int(first_num)):
    if el > int(last_num):
        break
    else:
        my_list.append(el)

print("Список : ", my_list)

print(f"Теперь этот список будем итерировать в цикле {iter_num} раза...")

с = 0
for el in cycle(my_list):
    if с >= len(my_list) * int(iter_num):
        break
    print(el)
    с += 1
