
my_string = 'test_11.1_dddd_1111_aaaa_test_1555_test_1844'

my_list = my_string.split('_')


text = my_list.count('test')
for i in range(text):
    my_list.remove('test')

for i in range(len(my_list)):
    if my_list[i].isdigit():
        my_list[i] = int(my_list[i])

print(my_list)
