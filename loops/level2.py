# %%
numbers = list(range(0, 101))
print(f"sum of Numbers from 0 to 100: {sum(numbers)}")
# %%
numbers = list(range(0, 101))
E_numbers = [num for num in numbers if num % 2 == 0]
print(f"sum of Even numbers from 0 to 100: {sum(E_numbers)}")
O_numbers = [num for num in numbers if num % 2 != 0]
print(f"sum of Odd numbers from 0 to 100: {sum(O_numbers)}")
# %%
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[::-1]  

# %%
