import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)

#pre = [1,2,3,10,18,28,27,47,33,43,37,42,27,31,13,12,8,7,2,4,1,1,1,1]
x = [60, 54, 46, 65, 62, 52, 46, 39, 64, 68, 54, 44, 52, 53, 42, 50, 50, 59,
43, 47, 40, 54, 47, 47, 51, 64, 59, 54,
47, 58, 58, 37, 40, 46, 47, 42, 45, 50,
34, 41, 46, 49, 50, 57, 49, 52, 55, 49,
45, 40, 44, 49, 60, 40, 48, 59, 49, 50,
48, 35, 61, 71, 61, 60, 50, 47, 44, 52,
51, 42, 45, 55, 52, 56, 56, 43, 49, 47,
37, 40, 55, 62, 52, 36, 49, 51, 40, 51,
35, 43, 52, 38, 59, 34, 36, 47, 39, 48]
#for i in range(len(pre)-3):
#    x+= [i+3]*pre[i]


print(x)
 # `density=False` would make counts

fig, ax = plt.subplots()
font = {'fontname': 'Times New Roman'}
#ax.set_title('Гистограмма вероятностей количества импульсов(t = 40 c)')
# Подписи:
ax.set_xlabel('Количество импульсов', **font)
ax.set_ylabel('Вероятность', **font)



# Сетка:
ax.minorticks_on()
ax.grid(True)
ax.grid(which='minor', linestyle = ':')


#plt.axis([0, 150, 0, 120])

plt.hist(x, density=True, color='blue', bins=20) 
plt.yticks([i/100 for i in range(0, 14, 2)])
plt.show()
