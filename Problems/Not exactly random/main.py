from random import randint
from random import seed


# don't modify this code or variable `n` may not be available
n = int(input())

seed(n)
print(randint(-100, 100))
