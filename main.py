import random
for m in range(10):
    print(random.randint(1, 100))

if m > 5:
    print("m is greater than 5")
else:
    print("m is less than or equal to 5")

guess = int(input("Enter a number between 1 and 100: "))
if guess == m:
    print("You guessed it!")
elif guess > m:
    print("Too high!")
else:
    print("Too low!")

print("The number was: ", m)
