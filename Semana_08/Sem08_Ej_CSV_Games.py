# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB


# Borrador de Pseudocódigo (general)
#1. Definir la lista de diccionarios
#2. Definir el diccionario
#3. Definir función para pedir la información del juego
#       3.1 Utilizar excepciones
#4. Definir función para unir las listas en un diccionario
#5. Definir función para incluir el nuevo diccionario a la lista
#6. Definir función para escribir el documento .csv
#7. Utilizar las funciones en orden (main)


############

#DUDAS:

#1. En las líneas 70 y 81 (las excepciones) no me arroja el mensaje de "Invalid value. Try again" cuando se digita un número que no es 1 o 2, solamnete cuando se digita otra tecla. Cómo corregir esto para que también lo haga cuando se digita un níumero diferente a las opciones dadas?

#2. La lista de keys se puede definir afuera de las funciones? antes de todo? o es mejor definirla dentro de las funciones que se van a utilizar específicamente? (aunq se repita?)

############



import csv



def ask_game_information ():
    name = input("Type the video game's name: ")
    genre = input("Type the genre of the video game: ")
    developer = input("Type the video game developer's name: ")
    esrb_rate = input("Type the video game ESRB rate: ")
    game_information_list_asked = [name,genre,developer,esrb_rate]
    return (game_information_list_asked)



def make_game_dictionary ():
    dictionary_game_asked = {}
    game_information_list = ask_game_information()
    counter = 0
    dictionary_keys = [
        "Name",
        "Genre",
        "Developer",
        "ESRB rate"
    ]

    for index in dictionary_keys:
        dictionary_game_asked [f"{index}"] = f"{game_information_list[counter]}"
        counter += 1
    
    return(dictionary_game_asked)



def make_my_list_of_games ():
    option_continue_writing = 1
    my_list_of_games = []

    while (option_continue_writing == 1):
        dictionary_game_information = make_game_dictionary()
        print (f"""The information of the game is: 
        {dictionary_game_information}""")

        while True:
            try:
                option_correct_data = int(input ("Is that information right? Press ( 1 ) for 'Yes' or ( 2 ) for 'Not': "))
                if option_correct_data == 1 or option_correct_data == 2:
                    break
            except:
                print("Invalid value. Try again")

        if option_correct_data == 1:
            my_list_of_games.append(dictionary_game_information)
    
        while True:
            try:
                option_continue_writing = int(input("Do you want to continue writing? Press ( 1 ) for 'Yes' ( 2 ) for 'Not': "))
                if option_continue_writing == 1 or option_continue_writing == 2:
                    break
            except:
                print("Invalid value. Try again")

    return (my_list_of_games)



def write_a_csv_file_from_a_list (file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)



def main ():
    print ("This program makes a .csv file from a list of video games you write")
    dictionary_keys = [
        "Name",
        "Genre",
        "Developer",
        "ESRB rate"
    ]

    final_list_of_games = make_my_list_of_games ()

    write_a_csv_file_from_a_list ("my_games.csv",final_list_of_games,dictionary_keys)

    print(f""""The complete data is:
        {final_list_of_games}

        A file named ' my_games.csv ' was made with this information.
            """)



if __name__ == "__main__":
    main()
