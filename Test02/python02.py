# Exercise 1: String Manipulation
def reverse_string(s):
    return s[::-1]

# Exercise 2: List Operations
def sum_of_list(lst):
    return sum(lst)

# Exercise 3: Dictionary Operations
def get_value(d, key):
    return d.get(key, "Key not found")

# Exercise 4: Tuple Operations
def tuple_to_list(t):
    return list(t)

# Exercise 5: Set Operations
def unique_elements(lst):
    return set(lst)

# Exercise 6: Integer Operations
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Exercise 7: Float Operations
def round_float(f, decimals):
    return round(f, decimals)

# Exercise 8: Boolean Operations
def is_even(n):
    return n % 2 == 0

# Exercise 9: Complex Number Operations
def add_complex(c1, c2):
    return c1 + c2

# Exercise 10: Type Conversion
def int_to_str(n):
    return str(n)