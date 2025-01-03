# В четвертій лабі замість цього зробити один з наступних алгоритмів для вашої функції на ваш вибір:
#  обернена інтерполяція або інтерполяція по Ерміту (деталі по ним в файлі-умові для 4 лаби).

#                                                   інтерполяція по ерміту
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

def f(x):
    return 1 / x

x = np.linspace(1, 5, 15)
y = f(x)

f_hermite = PchipInterpolator(x, y)

x_new = np.linspace(1, 5, 100)
y_hermite = f_hermite(x_new)

error_hermite = np.abs(f(x_new) - y_hermite)

f_hermite_der1 = f_hermite.derivative(1)
f_hermite_der2 = f_hermite.derivative(2)

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

axs[0].plot(x, y, 'o', label='Дані')
axs[0].plot(x_new, f(x_new), '--', label='Точна функція', color='gray')
axs[0].plot(x_new, y_hermite, label='Інтерполяція Ерміта', color='green')
axs[0].set_title('Інтерполяція Ерміта')
axs[0].legend()
axs[0].grid()

axs[1].plot(x_new, error_hermite, label='Похибка інтерполяції Ерміта', color='purple')
axs[1].set_title('Похибка інтерполяції Ерміта')
axs[1].legend()
axs[1].grid()

axs[2].plot(x_new, f_hermite_der1(x_new), label='Перша похідна', color='blue')
axs[2].plot(x_new, f_hermite_der2(x_new), label='Друга похідна', color='brown')
axs[2].set_title('Похідні інтерполяції Ерміта')
axs[2].legend()
axs[2].grid()

plt.tight_layout()
plt.show()
