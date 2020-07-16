'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
      Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
      Напишите решения через list и через dict. '''
print("\nУрок 2 Задание 3\n")

# создаём списки времён года (и месяцев)
season_list = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима' ]
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь' ]

# со словарём
season_dict = { 1 : 'январь, зима', 2 : 'февраль, зима', 3 : 'март, весна', 4 : 'апрель, весна', 5 : 'май, весна', 6 : 'июнь, лето',
                7 : 'июль, лето', 8 : 'август, лето', 9 : 'сентябрь, осень', 10 : 'октябрь, осень', 11 : 'ноябрь, осень', 12 : 'декабрь, опять зима' }

while True:
    try:
        month_num = int(input("Введите месяц числом\n"))
        if month_num < 1 or month_num > 12:
            raise  Exception
        # через списки - индексом будет элемента списка, который на 1 меньше номера месяца
        print(f"Месяц {month_num} это {month_list[month_num-1]}, и это {season_list[month_num-1]}")
        # через словари - тут не нужно никаких скрытых индексов т.к. задано прямое соответствие
        print(f"Через словари это {season_dict[month_num]}")
        break
    except ValueError:
        print('Неверный формат')
    except Exception:
        print('Номера месяцев на Земле от 1 до 12')
