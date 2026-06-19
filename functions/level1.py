# %%
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))
# %%
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2
print(area_of_circle(5))
# %%
def add_all_numbers(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            print("All arguments must be numbers")
            return None
    return sum(args)
print(add_all_numbers(1, 2, 3, 4.5))
# %%
def  convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convert_celsius_to_fahrenheit(25))
# %%
autumn = ["september", "october", "november"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["july", "august", "september"]
def check_season(month):
    month = month.lower()
    if month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    else:
        return "Invalid month"
print(check_season("October"))

# %%
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4))      
# %%
def solve_quadratic(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1} and {root2}"
print(solve_quadratic(1, -3, 2))

# %%
list1 = [1, 2, 3]
list2 = [4, 5, 6]
def print_list(lst):
    for item in lst:
        print(item)
print_list(list1)
print_list(list2)
# %%
def reverse_list(lst):
    return lst[::-1]    
print(reverse_list(list1))
# %%
def capitalize_list(lst):
    return [str(item).capitalize() for item in lst]
print(capitalize_list(["hello", "world"]))
# %%
