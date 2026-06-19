person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    print(f"the middle skill in the skill set is {person['skills'][int(len(person['skills'])//2)]}")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("You have Python skill")
    else:
        print("You don't have Python skill")


if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    if 'Node' not in person['skills'] and 'Python' not in person['skills'] and 'MongoDB' not in person['skills']:
        print('He is a front end developer')
    else:
        print('unknown title')  # Has frontend but also some backend (but not full stack)
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    if 'React' not in person['skills']:
        print('He is a backend developer')
    else:
        print('unknown title')
else:
    print('unknown title')
# %%
aim = {2,3,3,4,"hi","hello"}
print(list(aim))
print(list("joinaim"))

# %%
lst = range(0,11,2)
print(lst) # [0, 2, 4, 6, 8, 10]
print(lst[0]) # 0
# %%
print(set({'a': 1, 'b': 2, 'c': 3}))

# %%
