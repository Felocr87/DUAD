# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado

# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


def ask_for_a_number ():
    while True:
        try:
            number_asked = int(input("Type the second number for the mathematic operation (must be an integer): "))
            break
        except:
            print("Invalid value. Try again")
    return (number_asked)
    

def sum (actual_number):
    new_number = ask_for_a_number()
    result = actual_number + new_number
    print(f"{actual_number} + {new_number} =")
    print(result)
    return (result)


def subtract (actual_number):
    new_number = ask_for_a_number()
    result = actual_number - new_number
    print(f"{actual_number} - {new_number} =")
    print(result)
    return (result)


def multiply (actual_number):
    new_number = ask_for_a_number()
    result = actual_number * new_number
    print(f"{actual_number} * {new_number} =")
    print(result)
    return (result)


def divide (actual_number):
    new_number = ask_for_a_number()
    while new_number == 0:
        print("It is not posible divide by 0")
        new_number = ask_for_a_number()
    result = actual_number / new_number
    print(f"{actual_number} / {new_number} =")
    print(result)
    return (result)


def option_calculator_menu ():
    while True:
        try:
            print ("""
                These are the calculator options, what do you want to do?:
                1 Sum
                2 Subtract
                3 Multiply
                4 Divide
                5 Clear the calculator
                6 Exit
                """)
            option_number = int(input("Type the option number you want to do: "))
            
            my_list = [
                "Sum",
                "Subtract",
                "Multiply",
                "Divide",
                "Clear the calculator",
                "Exit"
                ]
            
            if option_number < 1  or option_number > 6:
                raise ValueError()
            else:
                print (f"Your option number is {option_number} {my_list[option_number-1]}")
                return (option_number)
            
        except:
            print("Invalid value option. Try again! (Remember typing an integer number according to the calculator options below)")


def calculate_process (original_number):

    actual_number = original_number

    while True:
        
        option_number = option_calculator_menu()
        
        if option_number == 1:
            result = sum(actual_number)
            actual_number = result
        
        elif option_number == 2:
            result = subtract(actual_number)
            actual_number = result

        elif option_number == 3:
            result = multiply(actual_number)
            actual_number = result
        
        elif option_number == 4:
            result = divide (actual_number)
            actual_number = result

        elif option_number == 5:
            actual_number = 0
            print (0)
        
        elif option_number ==6: 
            break
    exit


def main ():
    try:
        original_number = 0
        print ("Thanks for using this calculator program!")
        print (original_number)

        calculate_process (original_number)
        print("Thanks for using this program! Come back soon!")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")



if __name__ == "__main__":
    main()