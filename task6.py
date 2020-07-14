# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print("Задание 6\n")

start = float(input("Со скольки километров вы хотите начать?\n"))
end = float(input("До какой дистанции вы хотите добегаться?\n"))

day = 1
distance = start
print(f"\n{day}-й день: {distance} км.")

while distance < end:
    day +=1
    distance = (1.1 * distance)
    print(f"{day}-й день: {round(distance, 3)}")

print(f"\nОтвет: на {day}-й день спортсмен достиг результата — не менее {end} км")