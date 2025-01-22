import pandas as pd

""" чтение данных из CSV файла """
data = pd.read_csv('data.csv')

""" вывод всего файла """
print(data)

""" вывод первых 5 строк """
print(data.head())

""" вывод средней цены товара """
mean_unit_price = data['unit_price'].mean()
print(f'Среднее значение: {mean_unit_price}')

""" фильтрация данных: вывод строк, где цена товара меньше 10 """
filtered_data = data[data['unit_price'] < 10]
print(filtered_data)

### ---------------------------------------
import numpy as np

""" создание массива """
array = np.array([1, 2, 3, 4, 5])

""" возведение элементов массива в квадрат """
squared = array ** 2
print(f'Квадраты элементов: {squared}')

""" сумма элементов массива """
sum_array = np.sum(array)
print(f'Сумма элементов: {sum_array}')

""" среднее значение массива """
mean_array = np.mean(array)
print(f'Среднее значение: {mean_array}')

### ------------------------------------------
import matplotlib.pyplot as plt
""" данные для визуализации """
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

""" создание линейного графика """
plt.plot(x, y, marker='o')
plt.title('Простой линейный график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

""" сохранение графика в файл """
plt.savefig('plot.png')

""" отображение графика """
plt.show()