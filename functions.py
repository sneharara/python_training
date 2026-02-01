# 1. Function to print "SnehaRara"
def print_name():
    print("SnehaRara")

print_name()


# 2. Function that expects two arguments and prints them
def print_two_args(a, b):
    print(a, b)

print_two_args("Hello", "World")


# 3. Function that expects an unknown number of arguments
def print_args(*args):
    for item in args:
        print(item)

print_args(1, 2, 3, 4)


# 4. Function that expects keyword arguments (kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Sneha", age=20, gender="Female")


# 5. Function that expects a list as an argument
def print_list(lst):
    for item in lst:
        print(item)

print_list([10, 20, 30])


# 6. Function to find maximum of four numbers
def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print("Maximum:", max_of_four(10, 25, 7, 18))


# 7. Function to sum all numbers in a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print("Sum:", sum_list([1, 2, 3, 4, 5]))


# 8. Function to multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print("Product:", multiply_list([1, 2, 3, 4]))


# 9. Function to check whether a number falls in a given range
def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print(check_range(5, 1, 10))


# 10. Function to check whether a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(7)
