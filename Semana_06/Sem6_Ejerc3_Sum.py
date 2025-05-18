# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41


def get_a_list_of_numbers():
    quantity_of_numbers = int(input("How many numbers do you what to sum? "))

    list_of_numbers = []
    index = 0
    while index < quantity_of_numbers :
        number = int(input("Type a number to sum: "))
        list_of_numbers.append (number)
        index += 1

    return (list_of_numbers)


def sum_a_list_of_numbers(list_to_sum):
    
    sum = 0

    for number in list_to_sum:
        sum = sum + number

    print (f"The sum of the typed numbers is: {sum}")


list_of_numbers_to_sum = get_a_list_of_numbers()

sum_a_list_of_numbers(list_of_numbers_to_sum)