# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.


my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    'the last will be the first'
]
print(f'The original list is:{my_list}')

first_element = my_list.pop(0)

last_element = my_list.pop()

my_list.insert(0,last_element)

my_list.append(first_element)

print(f'The modified list is:{my_list}')

