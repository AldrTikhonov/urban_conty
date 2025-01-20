# """ Конечно, есть встроенная помощь """
import requests
# help(requests)
# # help(requests.get)

### --------------------------

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

func = some_function

### пример 1 - Атрибут класса __name__

print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(func.__name__)
# print(some_string.__name__)
# print(some_object.__name__)

### пример 2 - Узнаем тип объекта
# print(type(some_number))
#
# print(type(some_number) is int)
# print(type(some_number) is list)
#
# print(type(requests))
# print(type(requests.get))

### пример 3 - функция dir(), возвращает отсортированный список атрибутов и методов, доступных для указанного объекта, который может быть объявлен переменной или функцией.
from pprint import pprint

# pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
# pprint(dir(requests))

### Без указания аргумента dir() выводит доступные в локальной области видимости, как показано ниже
# pprint(dir())

### пример 4 - функция hasattr(), проверка на существование аттрибута
# attr_name = 'attribute_2'
# print(hasattr(some_object, attr_name))
# print(hasattr(some_object, 'attribute_1'))
# # pprint(dir(some_object))

### пример 4 - функция getattr(), получение атрибута
# print(getattr(some_object, 'attribute_1'))
# print(getattr(some_object, 'attribute_2', 'этого не может быть!'))

# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))
#
### пример 5 - функция callable(), проверка на то, что можем ли мы вызвать этот объект
# print(callable(some_string))
# print(callable(some_function))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_class_method))

### пример 6 - функция isinstance(), можем определить, является ли определенный объект экземпляром указанного класса
# print(isinstance(some_number, str))
# print(isinstance(some_number, int))
# print(isinstance(some_number, SomeClass))
# print(isinstance(some_object, SomeClass))

### пример 7 - модуль inspect - https://docs.python.org/3/library/inspect.html - этот модуль собирает удобные методы и классы для отображения интроспективной информации
# import inspect
# ### самые употребляемые функции
# # print(inspect.ismodule(requests))
# # print(inspect.isclass(requests))
# # print(inspect.isfunction(requests))
# # print(inspect.isbuiltin(requests))
#
# some_function_module = inspect.getmodule(some_function)
# print(type(some_function_module), some_function_module)

### ----- системный пакет sys ------------------- системный пакет sys ------------
import sys
# pprint(dir(sys))
#
# """ путь к интерпретатору Python """
# print(sys.executable)  # --> /home/user/.cache/pypoetry/virtualenvs/urban-conty-AyrHHL5T-py3.12/bin/python
#
# """ на какой операционной системе работаем """
# print(sys.platform)  # --> linux
#
# """ текущая версия Python """
# print(sys.version) # --> 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0]
# print(sys.version_info) # --> sys.version_info(major=3, minor=12, micro=3, releaselevel='final', serial=0)
#
# """ функция для отлова и сравнения версии """
# def func(x):
#     if sys.version.split(' ')[0] == '3.12.3':
#         return x + 10
#     else:
#         raise Exception('Недопустимая версия')
#
# print(func(10))
#
# """ список, содержащий параметры командной строки, если она была задана """
# print(sys.argv) # --> ['/home/user/urban_conty/Web/web_11_"Стандартные и сторонние библиотеки Python".py']
#
# """ путь поиска модуля, список каталогов, в которых Python будет искать модули во время импорта """
# print(sys.path) # --> ['/home/user/urban_conty/Web', '/home/user/urban_conty', '/usr/lib/python312.zip', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload', '/home/user/.cache/pypoetry/virtualenvs/urban-conty-AyrHHL5T-py3.12/lib/python3.12/site-packages']
#
# """ словарь, который отображает имена модулей в объекты модулей для всех загруженных в текущий момент модулей """
# print(sys.modules)
#
# """ __builtins__ - псевдо-модуль, содержащий встроенные в интерпретатор объекты (константы, исключения, функции)"""
# # print(__builtins__) # --> <module 'builtins' (built-in)>
# pprint(dir(__builtins__))

""" sys используется не только для того, чтобы узнать новую информацию """
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))