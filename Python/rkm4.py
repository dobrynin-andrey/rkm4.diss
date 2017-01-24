import math
import matplotlib.pyplot as plt
# Метод Рунге-Кутты 4-го порядка
# Пример dy/dx = sin(x)+cos(y), y(0)=5;


# Параметры
h = 0.1        # Размер шага
xfinal = 55     # Решать с x = [0, xfinal]

# Начальные значения
x = 0
y = 5

y0 = y

Xframe = [x]
Yframe = [y]
# Определим функцию ОДУ
function = math.sin(x)+math.cos(y)
lable_fun = str(math.sin(x)+math.cos(y))

def functionODU (x, y):
    f = function
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
# График результата

#plt.rc('font',**{'family':'verdana'})
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(Xframe, Yframe, "b-", label=lable_fun)
plt.legend()
plt.grid()
plt.show()


#plt.plot(Xframe, Yframe, 'r-')
#plt.show()
print ('Ответ: y('+ str(y0) + ') =', Yframe[-1])