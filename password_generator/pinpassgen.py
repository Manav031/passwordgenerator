import random

numbers = "1234567890"

length = int(input("enter length for the pin you want to generate: "))

if length == 4 or length == 6:
    pin = "".join(random.sample(numbers,length))
    print(f"your pin is {pin}")
else:
    print("select the length for pin between 4 to 6!!")