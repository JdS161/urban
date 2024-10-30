
# 3. Работа с множествами:
# - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
# - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
# - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
# - Удалите один любой элемент из множества my_set.
# - Выведите на экран измененное множество my_set.
#


# Set: {1, 'Яблоко', 42.314}
# Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}


my_dict = {'Fedor':1980, 'Michail': 1985, 'Markus':1987}
print('Dict:',my_dict)
print('Existing value:',my_dict.get('Fedor'))
print('Not existing value:',my_dict.get('Vadim'))
my_dict.update({'Vasili': 1990,
                'Egor': 1993})
deleted_value = my_dict.pop('Michail')
print('Deleted value:', deleted_value)
print('Modified dictionary:', my_dict)

my_set = {1, 'Two', 3.0, 1, 'Two', False}
print('\nSet:', my_set)
my_set.add(4)
my_set.add('New element')
my_set.discard(1)
print('Modified set', my_set)