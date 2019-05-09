import math


def square_root(a):
    print(math.sqrt(a))


is_input_correct = False

while is_input_correct:
    try:
        number = int(input("Please enter some number to square: "))
        print("squaring...")
        square_root(number)
        is_input_correct = True
    except ValueError:
        print('PLease input a valid integer')


l = [0, 9, 8, 1]

g = 0
for i in l:
    print(i)
    g = g + i

print("g = ", g)
