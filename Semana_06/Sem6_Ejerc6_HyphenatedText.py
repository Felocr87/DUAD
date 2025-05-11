# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual 
#   pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


original_text = "plato-vaso-tenedor-cuchillo"


def separate_hyphenated_text (hyphenated_text):

    list_of_words_without_hyphen = []

    word = ""

    for character in hyphenated_text:

        if character != "-":
            word = word + character
        else:
            list_of_words_without_hyphen.append (word)
            word = ""
        
    list_of_words_without_hyphen.append (word)

    return(list_of_words_without_hyphen)


def join_words_into_string (list_to_join):

    joined_string = ""

    for word in list_to_join:
        joined_string = joined_string + " " + word

    print(f"The final string is: {joined_string}")


def main ():
    print (f"The original text with hyphens was: {original_text}")

    original_list = separate_hyphenated_text(original_text)

    original_list.sort()

    join_words_into_string (original_list)



main()