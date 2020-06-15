import random

characters = "123456789"

length = int(input())

if length <= 9:
    pattern = "".join(random.sample(characters,length))
    print(pattern)
