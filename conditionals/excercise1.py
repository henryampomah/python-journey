# %% block1
while True:
    age = input("Enter your age: ")
    if int(age) >= 18:
        print("You are old enough to learn to drive.")
        continue
    else:
        print(f"You need {18 - int(age)} more years to learn to drive.")
        break

# %% block2
my_age = 18
your_age = int(input("Enter your age: "))

if your_age - my_age == 1:
    print("You are 1 year older than me.")
elif my_age - your_age == 1:
    print("I am 1 year older than you.")
elif your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")
elif my_age > your_age:
    print(f"You are {my_age - your_age} years younger than me.")
else:
    print("We are the same age.")
# %% block3
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 > number2:
    print(f"{number1} is greater than {number2}.")
elif number2 > number1:
    print(f"{number2} is greater than {number1}.")
else:
    print(f"{number1} is equal to {number2}.")

# %%
