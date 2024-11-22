def calculate_structure_sum(input_data):

    result = 0                                              # условие выхода из рекурсии
    if input_data ==0:
        return 0

    if isinstance(input_data, int):                         # проверка элемента структуры в случае int
        result += input_data
    elif isinstance(input_data, str):                       # проверка элемента структуры в случае str
        result += len(input_data)
    elif isinstance(input_data, (list, tuple, set)):        # проверка элемента структуры в случае list, tuple, set
        for item in input_data:
            result += calculate_structure_sum(item)
    elif isinstance(input_data, dict):                      # проверка элемента структуры в случае dict
        for key, value in input_data.items():
            result += calculate_structure_sum(key)
            result += calculate_structure_sum(value)

    return result


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
