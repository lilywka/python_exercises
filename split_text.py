
my_string = 'test_11.1_dddd_1111_aaaa_test_1555_test_1844'

my_new_list = []
my_list = my_string.split('_')

for elem in my_list:
    elem = elem.strip()
    my_new_list.append(elem)
print(my_new_list)


text = my_new_list.count('test')
for i in range(text):
    my_new_list.remove('test')

for i in range(len(my_new_list)):
    if my_new_list[i].isdigit():
        my_new_list[i] = int(my_new_list[i])

print(my_new_list)
