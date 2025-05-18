# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. 
#                   No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, 
#                   y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar 
#                   si el numero es primo o no.*


def get_a_list_of_numbers ():
# Esta funcion es para que el usuario ingrese la lista de numeros que desea comprobar

    quantity_of_numbers = int (input ("How many numbers do you what to type? "))

    list_of_numbers = []

    count = 0
    
    while count < quantity_of_numbers:
        number = int(input("Type a number (greater than 1): "))
        list_of_numbers.append(number)
        count += 1

    return(list_of_numbers)



def is_a_prime_number (number_to_check):
# Esta funcion define si los numeros son primos (devuelve true) o si son compuestos (devuelve false)

    square_root = number_to_check ** (1/2)

# Existe un teorema que indica que se puede comprobar si es un numero primo solamente con comprobar los numeros 
#   menores a la raiz cuadrada del numero que se esta revisando.
    
    if number_to_check == 2:
        number_is_prime = True

    if number_to_check == 3:
        number_is_prime = True

    else:
        
        counter = 2

        while counter <= square_root:

            if number_to_check % counter == 0:
                number_is_prime = False
                break

            else:
                number_is_prime = True
            counter += 1
    
    return (number_is_prime)



def select_prime_numbers ():
# Esrta funcion revisa los numeros de la lista ingressada y los compara si son numeros primos, ademas que 
#   tiene de output la impresion de la lista de numeros primos.    
    list_of_numbers = get_a_list_of_numbers()
    list_of_prime_numbers = []

    print(list_of_numbers)

    for number in list_of_numbers:
        if is_a_prime_number(number):
            list_of_prime_numbers.append(number)

    print (list_of_prime_numbers)



select_prime_numbers()