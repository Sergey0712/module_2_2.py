first = int(input('Введите первое число'))
second = int(input('Введите второе число'))
third = int(input('Введите третье число'))
if first == second and first == third:
    print('Все числа равны')
elif first == second or first == third or second == third:
    print(2)
else:
    print('Нет одинаковых чисел')