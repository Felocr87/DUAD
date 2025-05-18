# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0

    for index in range (0,len(text)) :

        character = text[index]

        if character.isupper():
            uppercase = uppercase + 1

        if character.islower():
            lowercase = lowercase + 1
        

    print (f"The quantity of upper case characters is: {uppercase}")
    print (f"The quantity of lower case characters is: {lowercase}")


count_uppercase_lowercase("a B c D E f g h I")


