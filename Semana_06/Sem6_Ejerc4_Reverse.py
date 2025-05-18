# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”


def reverse_a_string ():
	
    text_to_reverse = input("Type a text to reverse: ")
    new_text = ""
    
    for character in range (len(text_to_reverse)-1,-1,-1):
        new_text = new_text + text_to_reverse[character]
    
    print(new_text)


reverse_a_string()