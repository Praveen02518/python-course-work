import math

print(math.gcd(8,24))
print(math.log(2))
print(math.sin(45))
print(math.cos(0))
print(math.tan(45))

print(math.degrees(45))
print(math.radians(30))

#
import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

names=['varun', 'sachij', 'praveen', 'babu']

print(random.choices(names))
print(random.choices(names,k=3))

random.shuffle(names)
print(names)