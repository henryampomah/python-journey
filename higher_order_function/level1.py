# a map function takes a function and an iterable as input and applies the function to each element of the iterable, returning a new iterable with the results.
# a filter function takes a function and an iterable as input and returns a new iterable containing only the elements for which the function returns True.
# a reduce function takes a function and an iterable as input and applies the function cumulatively to the elements of the iterable, returning a single value.

# higher-order functions are functions that take other functions as arguments or return functions as their result. 
# closures are functions that capture the local variables from their enclosing scope, allowing them to access those variables even after the outer function has finished executing.
# decorators are a way to modify or enhance the behavior of functions or methods without changing their code. They are implemented as higher-order functions that take a function as input and return a new function with the desired modifications.


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# %%
for country in countries:
    print(country)
# %%
for name in names:
    print(name)
# %%
for number in numbers:
    print(number)



