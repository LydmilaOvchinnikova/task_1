#почему == а не is?
#а можно без километрового elif?
#считается ли обработкой некорректного результата ошибка, если первое значение - не число, а какой-то бред?
#считается ли обработкой некорректного результата ошибка, если делим на 0?
result = int(input ('vvedite pervoe chislo '))
if result is int:
    print("ок")
m = 0
while m!='=':
    m = input ('vvedite operatsiy i chislo ')
    if m!='=':
        m.split(',')
        m0 = m[0]
        m1 = int(m[1:])
        if m0 == '+':
            result += m1
        elif m0 == '-':
            result -= m1
        elif m0 == '/':
            result /= m1
        elif m0 == '*':
            result *= m1
        else: print('bred kakoy-to')
else: print(result)
