import math
# Метод Рунге-Кутты 4-го порядка
# Пример dy/dx = sin(x)+cos(y), y(0)=5;


# Параметры
h = 0.1        # Размер шага
xfinal = 1    # Решать с x = [0, xfinal]

# Начальные значения
x = 0
y = 1

Xframe = [x]
Yframe = [y]
# Определим функцию ОДУ
def functionODU (m, n):
    f = m + n
    return f

print (functionODU (x, y))
cail = math.ceil(xfinal/h)
print (cail)
# Цикл метода РК4

frame = list(range(int(cail)))
print (frame)


for i in range(math.ceil(xfinal/h)):
    # Обновим x
    print ('Это i: ', i)
    print ('Это x: ', x)

    print ('Это x: ', x)

    k1 = functionODU (x        , y           )
    print ('Это k1: ', k1)

    k2 = functionODU (m = (x + 0.5*h), n = (y + 0.5*k1*h))
    k3 = functionODU (m = (x + 0.5*h), n = (y + 0.5*k2*h))
    k4 = functionODU (m = (x +     h), n = (y +     k3*h))
    print ('Это у: ', y)

    y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    Yframe += [y]
    x = x + h;

    print ('Это х: ', x)
    print ('Это у: ', y)
    print ('Это k1: ', k1)
    print ('Это k2: ', k2)
    print ('Это k3: ', k3)
    print ('Это k4: ', k4)




                 # for i=1:ceil(xfinal/h)
#     # Обновим x
#     x(i+1) = x(i)+h;
#     # Обновим y
#     k1 = f(x(i)      , y(i)         );
#     k2 = f(x(i)+0.5*h, y(i)+0.5*k1*h);
#     k3 = f(x(i)+0.5*h, y(i)+0.5*k2*h);
#     k4 = f(x(i)+    h, y(i)+    k3*h);
#     y(i+1) = y(i)+h/6*(k1 + 2*k2 + 2*k3 + k4);
# end

# # График результата
# plot(x,y)
# xlabel('x')
# ylabel('y')
# a = 3
# print (a)
