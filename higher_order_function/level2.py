from functools import *
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
def uppercase_country(country):
    return country.upper()
uppercase_countries = list(map(uppercase_country, countries))
print(uppercase_countries)
# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_number(number):
    return number ** 2
squared_numbers = list(map(square_number, numbers))
print(squared_numbers)
# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def uppercase_name(name):
    return name.upper()
uppercase_names = list(map(uppercase_name, names))
print(uppercase_names)
# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def land_country(country):
    # return country.endswith('land')
        if 'land' in country:
            return True
        return False
land_countries = list(filter(land_country, countries))
print(land_countries)

# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
def six_letter_country(country):
    return len(country) == 6
six_letter_countries = list(filter(six_letter_country, countries))
print(six_letter_countries)

# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'elandr', 'elandnow']
def e_country(country):
    return country.startswith('E')
e_countries = list(filter(e_country, countries))
print(e_countries)
# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'lander']
from functools import reduce
result = map(lambda x: x.upper(),
                filter(lambda country: len(country) == 6, countries))
print(list(result))

# %%
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'elandre', 'elandnow']
result = map(lambda x: x.upper(),
                filter(lambda country: country.lower().startswith('e'),
                            filter(lambda country: 'land' in country, 
                                        filter(lambda country: len(country) >= 6, countries))))
print(list(result))

# %%
def get_string_lists(lst):
     return list(filter(lambda x: isinstance(x, str), lst))
example_list = ['Asabeneh', 1, 2, 'Finland', 'Sweden', 3, 4, 'Denmark', 'Norway', 5, 6, 'Iceland']
string_list = get_string_lists(example_list)
print(string_list)

# %%
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(lambda x, y: x + y, numbers)
print(total)
# %%
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries'
print(concatenated_countries)
print(countries[::-1])
# %%
from functools import reduce
from countries import countries
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))
print(categorize_countries('land'))
print(categorize_countries('ia'))
# %%
from countries import countries
dictionarized_countries = {country[0]: country[1:] for country in countries}
print(dictionarized_countries)

# %%
