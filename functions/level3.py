# %%
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime(12))
# %%
def is_unique(lst):
    return len(lst) == len(set(lst))
print(is_unique([1, 2, 3, 4]))
print(is_unique([1, 2, 3, 1]))
# %%
def same_dt(lst):
    if len(lst) == 0:
        return "The list is empty"
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return "Not all items are of the same data type"
    return "All items are of the same data type"
print(same_dt([1, 2, 3, 4]))
print(same_dt([1, "2", 3, 4]))
# %%
def python_variable(variable):
    if variable.isidentifier() and not variable in ["False", "None", "True"]:
        return f"{variable} is a valid Python variable name"
    else:
        return f"{variable} is not a valid Python variable name"
print(python_variable("my_var"))
print(python_variable("123var"))
# %%


def most_spoken_languages(countries, n):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]
print(most_spoken_languages(countries, 10))
# %%
