import random
from typing import Mapping
def randInt(min=0, max=100):
    if min == 0 and max == 100:
        num = random.random() * 100
        return round(num)
    elif max < 0:
        print("Max value must be greater than 0")
    elif min > max:
        print("Max value must be greater than min value")
    elif min == 0 and max != 100:
        num = random.random() * max
        return round(num)
    elif min != 0 and max == 100:
        num = (random.random() * (100-min) + min)
        return round(num)
    elif min!=0 and max != 100:
        num = (random.random() * (max-min) + min)
        return round(num)

print(randInt()) # should print a random integer between 0 to 100
print(randInt(max=50)) # should print a random integer between 0 to 50
print(randInt(min=50)) # should print a random integer between 50 to 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500