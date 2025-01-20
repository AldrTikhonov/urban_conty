import inspect

# def introspection_info(obj):
#     """
#     Функция принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта,
#     чтобы определить его тип, атрибуты, методы, модуль и другие свойства
#     """
#     obj_type = type(obj)

obj = 45
obj_type = type(obj)
print(obj_type)
print(obj).__name__
