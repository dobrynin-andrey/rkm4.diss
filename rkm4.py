import math
# Метод Рунге-Кутты 4-го порядка
# Пример dy/dx = sin(x)+cos(y), y(0)=5;


# Параметры
h = 0.1        # Размер шага
xfinal = 1     # Решать с x = [0, xfinal]

# Начальные значения
x = 0
y = 5

Xframe = [x]
Yframe = [y]
# Определим функцию ОДУ
def functionODU (x, y):
    f = math.sin(x)+math.cos(y)
    return f

# Цикл метода РК4
for i in range(math.ceil(xfinal/h)):

    k1 = functionODU (x        , y           )
    k2 = functionODU (x + 0.5*h, y + 0.5*k1*h)
    k3 = functionODU (x + 0.5*h, y + 0.5*k2*h)
    k4 = functionODU (x +     h, y +     k3*h)

    y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    # Поместим y в массив
    Yframe += [y]
    # Поместим x в массив
    Xframe += [x]
    # Обновим x
    x = x + h;

print ('Это х: ', Xframe)
print ('Это у: ', Yframe)
'''
    print ('Это k1: ', k1)
    print ('Это k2: ', k2)
    print ('Это k3: ', k3)
    print ('Это k4: ', k4)
'''
# # График результата
# plot(x,y)
# xlabel('x')
# ylabel('y')