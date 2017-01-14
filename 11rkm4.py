import math
# Метод Рунге-Кутты 4-го порядка
# Пример dy/dx = sin(x)+cos(y), y(0)=5;


# Параметры
h = 0.1        # Размер шага
xfinal = 55    # Решать с x = [0, xfinal]

# Начальные значения
x = 0
y = 5

# Определим функцию ОДУ
def functionODU (x, y):
    f = math.sin(x)+math.cos(y)
    return f
print (functionODU (x, y))
# Цикл метода РК4
while i :math.ceil(xfinal/ h)):
    pass

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
a = 3
print (a)
