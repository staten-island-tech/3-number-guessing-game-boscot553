import random
x = random.randint(1, 100)
answer = input("Pick a number ")
x = int(x)
answer = int(x)
while answer is not x:
    if answer > x:
        answer = input("The number is less, try again ")
    else: 
        answer = input("The number is greater, try again ")

print(x)

