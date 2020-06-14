import random

characters = "abcdefghijklmnopqrstvuwxyz1234567890ABCDEFGHJIKLMNOPQRSTUVWXYZ@#!"

length = int(input("enter length of password: "))

if length <= 18 and length >= 8:
    password = "".join(random.sample(characters,length))
    print(f"Your password is {password}")
else:
    print("Please select length between 8 to 18 to create a strong Password")