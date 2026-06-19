# %%
def even_and_odd(num):
    evens = (num // 2) +1
    odds = (num + 1) // 2
    return f"{evens} number of even numbers and {odds} number of odd numbers"
print(even_and_odd(10))
# %%
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))
# %%
def is_empty(para):
    if len(para) == 0:
        return "The parameter is empty"
    else:
        return "The parameter is not empty"
print(is_empty(""))
print(is_empty("Hello"))
# %%
def mini_stats(list):
    if len(list) == 0:
        return "The list is empty"
    mean = sum(list) / len(list)
    sorted_list = sorted(list)
    mode = max(set(list), key=list.count)
    standard_deviation = (sum((x - mean) ** 2 for x in list) / len(list)) ** 0.5
    median = sorted_list[len(sorted_list) // 2] if len(sorted_list) % 2 != 0 else (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    variance = sum((x - mean) ** 2 for x in list) / len(list)
    range = max(list) - min(list)
    return f"Mean: {mean},Sorted List: {sorted_list}, Mode: {mode}, Standard Deviation: {standard_deviation}, Median: {median}, Variance: {variance}, Range: {range}"
print(mini_stats([1, 2, 3, 4, 5, 5]))

# %%
def greet(name):
    if name == "":
        return "Hello, Guest!"
    return f"Hello, {name}!"
print(greet("Alice"))
print(greet(""))

# %%
def show_args(**args):
    result = []
    for key, value in args.items():
        result.append(f"{key}: {value}")
    return f"Received: {', '.join(result)}"
print(show_args(name="Alice", age=30, city="New York"))
# %%

