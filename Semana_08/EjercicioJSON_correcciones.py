#Esta es la versión del programa para abrir , agregar en guardar JSON, con las correcciones del profesor

import json
import os


def ask_for_pokemon_information():
    print("\nWrite the information of the new pokemon:")
    name_in_english = input("Name (in english): ")
    pokemon_type = input("Pokemon type: ")
    base_hp = input("HP: ")
    base_attack = input("Attack: ")
    base_defense = input("Defense: ")
    base_sp_attack = input("Sp. Attack: ")
    base_sp_defense = input("Sp. Defense: ")
    base_speed = input("Speed: ")

    return {
        "name": {"english": name_in_english},
        "type": [pokemon_type],
        "base": {
            "HP": base_hp,
            "Attack": base_attack,
            "Defense": base_defense,
            "Sp. Attack": base_sp_attack,
            "Sp. Defense": base_sp_defense,
            "Speed": base_speed
        }
    }

def load_pokemon_data(filename):
    try:
        # Si el archivo no existe o está vacío, retornar lista vacía
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return []
        
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: El archivo contiene JSON inválido. Se creará uno nuevo.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def save_pokemon_data(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("\nPokemon added properly!")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def main():
    filename = 'pokemones.json'
    
    # Cargar datos existentes o crear nueva lista
    pokemon_data = load_pokemon_data(filename)
    print("\nCurrent Pokemon data:", pokemon_data)
    
    # Agregar nuevo pokémon
    new_pokemon = ask_for_pokemon_information()
    pokemon_data.append(new_pokemon)
    
    # Guardar datos actualizados
    save_pokemon_data(filename, pokemon_data)
    
    # Mostrar datos actualizados
    print("\nUpdated Pokemon data:", pokemon_data)

if __name__ == "__main__":
    main()