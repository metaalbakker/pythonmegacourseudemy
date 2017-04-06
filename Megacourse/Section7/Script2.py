import random
import string

medeklinkers = 'bcdfghkjlmnpqrstvwxz'
klinkers = 'aeiouy'
alfabet = medeklinkers+klinkers #of string.ascii_lowercase

letter_input_1 = input("Wat voor letter wil je als eerst? (m)edeklinker, (k)linker of (g)ewoon maar iets?")
letter_input_2 = input("Wat voor letter wil je als eerst? (m)edeklinker, (k)linker of (g)ewoon maar iets?")
letter_input_3 = input("Wat voor letter wil je als eerst? (m)edeklinker, (k)linker of (g)ewoon maar iets?")

def generator():

    if letter_input_1=='m':
        letter1 = random.choice(medeklinkers)
    elif letter_input_1=='k':
        letter1 = random.choice(klinkers)
    elif letter_input_1=='g':
        letter1 = random.choice(alfabet)
    else:
        letter1 = letter_input_1

    if letter_input_2=='m':
        letter2 = random.choice(medeklinkers)
    elif letter_input_2=='k':
        letter2 = random.choice(klinkers)
    elif letter_input_2=='g':
        letter2 = random.choice(alfabet)
    else:
        letter2 = letter_input_2

    if letter_input_3=='m':
        letter3 = random.choice(medeklinkers)
    elif letter_input_3=='k':
        letter3 = random.choice(klinkers)
    elif letter_input_3=='g':
        letter3 = random.choice(alfabet)
    else:
        letter3 = letter_input_3

    name = letter1 + letter2 + letter3

    return name

print(generator())