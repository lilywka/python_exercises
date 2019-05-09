def check_division(l):
    for i in l:
        if i % 15 == 0:
            print('fizz-buzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')

        else:
            print(i)


def swap_dict(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        result_dict[value] = key
    return result_dict


check_division(range(1, 100))
dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
result = swap_dict(dict1)
print(result)
