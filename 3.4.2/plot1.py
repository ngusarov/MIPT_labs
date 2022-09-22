#Строит графики: 
#https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html - хороший сайт
#https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py - оф.документация
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10,7)) #Настраивает размер графика, можно сделат побольше
plt.grid(True) #Включает разметку

#Массив значений по х
X = [283.296,
285.068,
287.126,
289.116,
291.174,
293.068,
295.048,
297.058,
299.058,
301.14,
303.072,
305.13,
307.024,
309.038,
311.014,
312.98
]
#Массив погрешности каждой точки по х (можно ввести только одно число, если погрешность единая)
X_err = 0.01

#Массив значений по y
Y = [0.027613271,
0.028135834,
0.029256126,
0.031297405,
0.035557831,
0.044457596,
0.066957391,
0.108926577,
0.151846937,
0.194416362,
0.232213869,
0.27199849,
0.305796277,
0.342465753,
0.375593061,
0.406442107
]
#I1 = [5*i for i in I1]
#Массив погрешности каждой точки по y (можно ввести только одно число, если погрешность единая)
Y_err = 0.1


#Массив значений для псевдо прямой
X1 = [0, 1]
#Массив погрешности каждой точки по y (можно ввести только одно число, если погрешность единая)
X1_err = 0

#Массив значений по I3
Y1 = [0, 1037.88]
#Массив погрешности каждой точки по y (можно ввести только одно число, если погрешность единая)
Y1_err = 0


#Нарисует график, можно подписать график или сменить цвет
#Насчет fmt и marker, их можно заменять. fmt - только точки, marker - точки+линия
plt.errorbar(X, Y, xerr = 0.01, yerr = 0, fmt = 'o', markersize = None, color ='blue', label = u'Зависимость тока I')
plt.errorbar([314, 291.75], [0.441,0], xerr = 0, yerr = 0, fmt = '-', markersize = None, color ='pink', label = u'Зависимость тока на катушке')
#plt.errorbar(X, I3, xerr = X_err, yerr = I3_err, fmt = 'o', markersize = None, color ='green', label = u'Зависимость тока на конденсаторе ')

#Сюда можно ещё раз вставить операцию с рисованием графика
#plt.title(r'$Зависимость\:I(x)$', size = 20)
#Где расположить подпись к графику (ПОСЛЕ ТОГО, как описали все графики)
#plt.legend(loc = 'upper left')
#Подпись к оси х
plt.xlabel(r'$T,\:\:K$', fontsize = 16)
#Подпись к оси y
plt.ylabel(r'$f(T),\:\:us^{-2}$', fontsize = 16)
#Увеличивает размер шрифта координатных осей (надо поставить цифру в labelsize)
plt.tick_params(axis='both', which='major', labelsize=None)
plt.savefig("plot1.png")
plt.show()
