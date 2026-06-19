# %%
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
test_list = [1, 2, 3, 4, 5]
print(shuffle_list(test_list))
# %%
import random
def random_int():
    return random.randint(0, 9)
random_int()
# %%
from random import sample

def seven_random_numbers():
    return sample(range(10), 7)

print(seven_random_numbers())  
# %%
