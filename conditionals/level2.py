# %% block1
choice = input("is your score percentagewise? (y/n)")
if choice == "y":
    score = int(input("Enter your score: "))
    if score >= 80:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 60:
        print("C")
    elif score >= 50:
        print("D")
    else:
        print("F")
elif choice == "n": 
    max_score = int(input("Enter the maximum possible score: "))
    score = int(input("Enter your score: "))
    if score < 0 or score > max_score:
        print(f"Enter an actual score (must be between 0 and {max_score})")
    else:
        percentage = (score / max_score) * 100
        print(f"Your score: {score}/{max_score} = {percentage}%") 
    if percentage >= 80:
        print("A")
    elif percentage >= 70:
        print("B")
    elif percentage >= 60:
        print("C")
    elif percentage >= 50:
        print("D")
    else:
        print("F")
else:
    print("Invalid input")
    print("Enter y for yes or n for no")
# %% block2
month = input("Enter a month: ")
if month == "september" or month == "october" or month == "november":
    print("It is Autumn")
elif month == "december" or month == "january" or month == "february":
    print("It is Winter")
elif month == "march" or month == "april" or month == "may":
    print("It is Spring")
elif month == "june" or month == "july" or month == "august":
    print("It is Summer")
else:
    print("Invalid input")

# %%
fruits = ["mango", "banana", "apple", "orange"]

fruit = input("Enter a fruit: ")

if fruit not in fruits:
    fruits.append(fruit)

print(fruits)

# %%
