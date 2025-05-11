counter = 1
amount_achieved = 0
amount_failed = 0
sum_achieved = 0
sum_failed = 0
sum_total = 0

print("This program calculates the average of achieved and failed grades for each student.")
amount_grades = int(input("How many grades do you want to type? "))

while(counter <= amount_grades):
    grade = int(input(f"Type the grade {counter} (without decimals): "))
    if(grade >= 70):
        amount_achieved += 1
        sum_achieved = sum_achieved + grade
    else:
        amount_failed += 1
        sum_failed = sum_failed + grade
    sum_total = sum_total + grade
    counter += 1

if(amount_achieved != 0):
    average_achieved = sum_achieved / amount_achieved

else:
    average_achieved = "There are not achieved grades"


if(amount_failed != 0):
    average_failed = sum_failed / amount_failed

else:
    average_failed = "There are not failed grades"


general_average = sum_total / amount_grades

print("The achieved grades amount is:",amount_achieved)
print("The failed grades amount is:",amount_failed)
print("The achieved average grade is:",average_achieved)
print("The failed average grade is:",average_failed)
print("The general average grade is:",general_average)
