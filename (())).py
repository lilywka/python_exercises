a = ['(', '(', ')', ')', ')']

opened = []
closed = []
for el in a:
    if el == '(':
        opened.append(el)
    elif el == ')':
        closed.append(el)
n = len(opened) - len(closed)
print(n)
my_list = []
bracket = ''
if len(opened) > len(closed):
    bracket = '('
elif len(opened) < len(closed):
    bracket = ')'
i = 0
while i < abs(n):
    my_list.append(bracket)
    i += 1
# cleaned[0] = '()'

print(opened)
print(closed)
print(my_list)
