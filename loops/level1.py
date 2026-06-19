# %%
for i in range(0,11):
    print(i)
iterated = 0
while iterated < 11:
    print(iterated)
    iterated+= 1
# %%
for i in range(10,0,-1):
    print(i)
iterated = 10
while iterated >= 0:
    print(iterated)
    iterated-= 1
# %%
hashtag = "#"
for i in range(0,7):
    print(hashtag)
    hashtag += "#"
# %%
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()  # Print a newline after each row
# %%
for i in range(8):
    print("# " * 8)  # Print 8 hashes with spaces
# %%
for i in range(12):
    print(f"{i} x {i} = {i*i}")
# %%
frameworks =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(len(frameworks)):
    print(frameworks[i])
# %%
for i in range(len(frameworks)-1, -1, -1):
    print(frameworks[i])
# %%
for i in range(1, 100):
    if i % 2 == 0:
        print(i)
# %%
for i in range(1, 100):
    if i % 2 != 0:
        print(i)
# %%