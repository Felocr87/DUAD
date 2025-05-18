import random

number_random = random.randint(0,10)

number_user = int(input("Try to guess my secret number from 0 to 10: "))

while(number_user != number_random):
    number_user = int(input("No no! Try again: Guess my secret number from 0 to 10: "))

print(f"Congratulations! The secret number is: {number_user}!!!")