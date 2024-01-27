from random import randint as RI

NUMBERS = 1000
RAND_RANGE = 100

list_numbers = [RI(1, RAND_RANGE + 1) for n in range(1, NUMBERS + 1)]
