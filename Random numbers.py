
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)   # Have to change seed to generate a different range of numbers
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)
