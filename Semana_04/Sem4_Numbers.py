print("Type three numbers to know the largest one")
number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))

largest_number = number1
if(largest_number < number2):
    largest_number = number2
if(largest_number < number3):
    largest_number = number3

print("The largest number is:",largest_number)