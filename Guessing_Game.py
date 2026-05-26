import random
import datetime

num = random.randint(1, 10)
time = datetime.datetime.now()

print("Welcome To Guessing Number Game..!")

attempts = 5

while attempts > 0:
    try:
        number = int(input("Enter number between 1 to 10: "))

        if number == num:
            print("CONGRATULATIONS! You Win")
            print("Time:", time)
            break

        elif number > num:
            print("Too High!")

        else:
            print("Too Low!")

        attempts = attempts - 1
        print("Remaining Attempts:", attempts)

    except ValueError:
        print("Please Enter Valid Number..!")

if attempts == 0:
    print("Game Over..!")

print("Correct Number is:", num)