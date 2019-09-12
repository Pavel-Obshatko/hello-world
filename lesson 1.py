# print('Hello word')
# a = 2
# b = 3
# print(a + b)

# Задание 1
print('Добрый день')
num = int(input('Введите пожалуйста число: '))
print(num + 2)

year = 18
age = int(input('Введите ваш возраст пожалуйста: '))

if age >= year:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

# Задание 2

number = int(input('Введите число от 0 до 10: '))
while number < 0 or number > 10:
    number = int(input('Попробуйте ещё раз: '))
print('Молодец, все верно!')

print(number ** 2)

a = int(input('Введите первое число от 0 до 10: '))
b = int(input('Введите второе число от 0 до 10: '))
# print('первое число: ', b, 'второе число: ', a)
a, b = b, a
print('Первое число: ', a)
print('Второе число:', b)

