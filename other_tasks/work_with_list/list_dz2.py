
my_list = ['test', ' omagad!!! ', '123', 16, 'pRIVET']

print(my_list)

my_list.append(0.23)
my_list[1] = my_list[1].strip()
my_list[1] = my_list[1].upper()
my_list[2] = float(my_list[2])
my_list[3] = str(my_list[3])
my_list[4] = my_list[4].capitalize()
my_list = list(reversed(my_list))

print(my_list)
