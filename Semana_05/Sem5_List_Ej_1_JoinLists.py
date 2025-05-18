# 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.


even_numbers = [
    1,
    3,
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
]

odd_numbers= [
    0,
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
]

for index in range (0,len(odd_numbers)):
    print(odd_numbers[index],even_numbers[index])