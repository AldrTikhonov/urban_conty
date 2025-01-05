### ----------- библиотека datetime ---------- библиотека datetime ----------
from datetime import date
#
# """ вывод даты """
# my_date_1 = date(2024, 10, 31)
# my_date_2 = date(day=1, month=1, year=2025)
# print(my_date_1)
# print(my_date_2)
# print(type(my_date_1))
#
# """ вывод отдельно месяц, день и год """
# print(my_date_1.month)
# print(my_date_1.day)
# print(my_date_1.year)
#
# """ вывод сегодняшней даты """
# lesson_date = date.today()
# print(lesson_date)
#
# """ вывод дня недели цифрами, начиная с 1 (от 1 до 7 вкл)"""
# print(lesson_date.isoweekday())
# print(my_date_1.isoweekday())
#
# """ вывод максимальной и минимальной даты """
# print(date.min)
# print(date.max)

# """ вывод даты по номеру дня """
# my_date_3 = date.fromordinal(900)
#
# print(my_date_3)
# print(my_date_2.toordinal())

### ---------------------------------------------
from datetime import time, date
#
# """ вывод времени """
# my_time_1 = time(minute=40, second=20, hour=15)
# my_time_2 = time(11, 25, 50, 2024)
# my_time_3 = time(11, 25, 50)
# my_time_4 = time(11, 25)
# my_time_5 = time(11)
# my_time_6 = time()
# my_time_7 = time(second=56)
#
# print(type(my_time_1))
# print(my_time_1, my_time_2, my_time_3, my_time_4, my_time_5, my_time_6, my_time_7, sep='\n')
# print(my_time_2.minute)
# print(my_time_2.second)
#
# """ сравнение времени и даты """
# my_date_4 = date.today()
# my_date_5 = date(2024,12,31)
#
# print(my_time_1 > my_time_2)
# print(my_date_4 > my_date_5)
#
# """ вывод даты и времени в компьютерном виде """
# print(repr(my_date_4))
# print(repr(my_time_1))
#
# """ вывод дат в виде списка, СОРТИРОВКА """
# my_dates = [date(2024, 12,25), date(2025, 1, 1), date.today()]
# print(my_dates)
# print(*my_dates, sep='\n')
# print(min(my_dates))
# print(max(my_dates))
# print(sorted(my_dates))

# """ вывод дат в виде множества"""
# my_set = {date(2024, 12, 25), date(2025, 1, 1), date.today()}
# print(my_set)
# print(*my_set, sep='\n')
#
# """ вывод дат в виде словаря """
# my_dict = {date(2024, 12, 25): 'Good day', date(2025, 1, 1): "New Year", date(2025,1,3): 'Today'}
# print(my_dict)
# print(*my_dict, sep='\n')
#
# """ изменение даты и времени методом replace """
# date_1 = date(2023, 5, 15)
# date_2 = date_1.replace(year=2024, month=12, day=31)
# time_1 = time(10, 20, 30)
# time_2 = time_1.replace(minute=50)
#
# print(date_1, date_2, time_1, time_2, sep='\n')

### --------- библиотека os ------------- библиотека os -------------
import os
#
# """ вызов тип нашей системы """
# print(os.name)
#
# """ название нашей директории """
# print(os.getcwd()) # --> /home/user/urban_conty/Web
#
# """ смена рабочей директории """
# os.chdir('/home/user/urban_conty')
# print(os.getcwd()) # --> /home/user/urban_conty
# os.chdir('/home/user/urban_conty/Web') # вернемся обратно в нашу рабочую директорию
# print(os.getcwd()) # --> /home/user/urban_conty/Web
#
# """ проверка существования пути """
# print(os.path.exists('/home/user/urban_conty/poetry.lock')) # --> True
# print(os.path.exists('home/user/urban_conty/test_1.txt')) # --> False
#
# """ получение полного (абсолютного) пути """
# print(os.path.abspath("pyprojecr.md")) # --> /home/user/urban_conty/Web/pyprojecr.md
#
# """ проверка является ли файл файлом """
# print(os.path.isfile("/home/user/urban_conty/Web/test.txt") # --> True (файл test.txt создали предворительно в ручную)
#
# """ проверка директории """
# print(os.path.isdir("/home/user/urban_conty/Web"))
# print(os.path.isdir("/home/user/urban_conty"))
#
# """ создание новой директории """
# os.mkdir("/home/user/urban_conty/Web/Dir_1") # директория создалась по указанному пути
#
# """ удаление файла test.txt"""
# os.remove("/home/user/urban_conty/Web/test.txt") # файл test.txt удален
#
# """ удаление папки, каталога, директории """
# os.rmdir("/home/user/urban_conty/Web/Dir_1") # удалили директорию
os.rmdir("/home/user/test_05_1")

