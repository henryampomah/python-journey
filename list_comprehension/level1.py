

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = filter(lambda x: x <= 0, numbers)
print(list(negative_numbers))
# %%
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = lambda lst: [item for sublist in lst for item in sublist]
print(flattened_list(list_of_lists))
# %%
table = [tuple([base] + [base**exp for exp in range(6)]) for base in range(11)]
print(table)
# %%
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = []
for country in countries:
    for name, capital in country:
        transformed = (name.upper(), name[:3].upper(), capital.upper())
        result.append(transformed)

print(result)
# %%
countries_dictionary = []
for country in countries:
    for name, capital in country:
        transformed = {
            'country': name.upper(),
            'city': capital.upper()
        }
        countries_dictionary.append(transformed)

print(countries_dictionary)
# %%
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = []
for name in names:
    for first_name, last_name in name:
        full_name = f"{first_name} {last_name}"
        names_concatenated.append(full_name)
# %%
print(names_concatenated)
# %%
