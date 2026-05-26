import random
import datetime

num=random.randint(1,10)
time=datetime.datetime.now()

print("Welcome To Gussing Number Game..!")

number=int(input("Enter Number Between 1 to 10"))

if number==num:
    print("CONGRALUTAION You Are WIN")
    print("Time:",time)

else:
    
    print("Try Again..!")

print("The Number is:-",num)
