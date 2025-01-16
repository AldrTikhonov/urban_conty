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

# print(some_function.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(func.__name__)
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
import inspect
### самые употребляемые функции
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isfunction(requests))
# print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)