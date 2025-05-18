#Este programa importa un archivo JSON y le agrega una nueva entrada de información


import json


def ask_for_pokemon_information ():
    print("Write the information of the new pokemon:")
    name_in_english = input("Name (in english): ")
    pokemon_type = input ("Pokemon type: ")
    base_hp = input("HP: ")
    base_attack = input("Attack: ")
    base_defense = input("Defense: ")
    base_sp_attack = input("Sp. Attack: ")
    base_sp_defense = input("Sp. Defense: ")
    base_speed = input("Speed: ")

    name = {"english" : name_in_english}
    type = [pokemon_type]
    base = {
        "HP": base_hp,
        "Attack": base_attack,
        "Defense": base_defense,
        "Sp. Attack": base_sp_attack,
        "Sp. Defense": base_sp_defense,
        "Speed": base_speed
        }

    pokemon_information = {
        "name": name,
        "type": type,
        "base": base,
                }

    return (pokemon_information)


with open('pokemones.json', 'r', encoding='utf-8') as file:
    initial_data = json.load(file)

print(initial_data)

new_pokemon = ask_for_pokemon_information()

initial_data.append(new_pokemon)

print (initial_data)


with open('pokemones.json', 'w', encoding='utf-8') as file:
    json.dump(initial_data, file, indent=4, ensure_ascii=False)

print ("Pokemon added properly")