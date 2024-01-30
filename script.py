import random

def get_double(number: int):
    return number * 2

myRandomNumber = random.randint(1, 100)

print(f'My random number is {myRandomNumber} and its double is {get_double(myRandomNumber)}')