# 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
#   seguido del numero ingresado más alto.

my_list = []
counter = 0

largest_number = 0


while (counter < 10):
    number = int(input("Type a number: "))
    my_list.append(number)
    
    if(number > largest_number):
        largest_number = number 

    counter += 1


print(f'The typed numbers are: {my_list}')
print(f'The largest number is {largest_number}')