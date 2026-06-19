from random import *
from string import ascii_letters, digits
def random_user_id():
    return ''.join(choices(ascii_letters + digits, k=6))
print(random_user_id())
print(random_user_id())
# %%
from random import *
from string import ascii_letters, digits
def user_id_gen_by_user():
    try:
        num_ids = int(input("Enter the number of IDs you want to generate: "))
        id_length = int(input("Enter the length of each ID: "))
        for _ in range(num_ids):
            print(''.join(choices(ascii_letters + digits, k=id_length)))
    except ValueError:
        print("Please enter valid integers for the number of IDs and their length.")
user_id_gen_by_user()
# %%
# from random import *
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f"rgb({r}, {g}, {b})"
print(rgb_color_gen())

