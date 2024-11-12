# Домашнее задание по уроку "Распаковка позиционных параметров".
#
#
#
# Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.
#
#
#
# Задача "Распаковка":
#
# 1.Функция с параметрами по умолчанию:
#
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# 2.Распаковка параметров:
#
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
# 3.Распаковка + отдельные параметры:
#
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
# Пример результата выполнения программы:
#
# Исходный код:
#
# values_list_2 = [54.32, 'Строка' ]
#
# print_params(*values_list_2, 42)
#
# Вывод на консоль:
#
# 54.32 'Строка' 42
#
#
#
# Примечания:
#
# Использование параметров по умолчанию позволяет функциям быть гибкими и удобными в использовании.
# Распаковка параметров из списка и словаря позволяет передавать группы значений в функцию, что упрощает работу с данными.
# Важно!
#
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
#
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
#
# def a(my_list = [])) – это приводит к ошибкам!
#
#
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
#
# def append_to_list(item, list_my=None):
#
#   if list_my is None:
#
#    list_my = []
#
#   list_my.append(item)
#
# print(list_my)
#
#
#
# Файл module_3_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
#
#
#
# Успехов!
#
