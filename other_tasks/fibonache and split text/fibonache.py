
def generate_fibonacci(limit):
    fibonacci_list = [0]
    fib = 1
    i = 0
    while fib < limit:
        fibonacci_list.append(fib)
        fib = fibonacci_list[i] + fibonacci_list[i + 1]
        i = i + 1
    return fibonacci_list


print(generate_fibonacci(100))
