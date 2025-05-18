
# En este programa sí tuve q ayudarme con ChatGPT



list_of_pets = [
    "Cats",
    "Dogs",
    "Hamsters",
    "Fishes",
]

animals_in_the_reserve = {
    "Birds" : 200,
    "Turtles": 5,
    "Cats" : 10,
    "Tigers": 0,
    "Sloths" : 2,
    "Dogs" : 8,
}

pets_in_the_reserve = {}

# asi tenia mi codigo inicialmente:

# for animal in animals_in_the_reserve.keys():

#     for pet in list_of_pets:

#         if animal == pet :
            
#             animals_in_the_reserve.pop(animal)

# print(animals_in_the_reserve)


animals_to_remove = []  
# esta lista fue recomendacion de ChatGPT, para eliminar las keys del diccionario en un segundo ciclo for, 
#   y así no afectar las iteraciones del primer ciclo for.



for animal in animals_in_the_reserve.keys():
    
    for pet in list_of_pets:
        
        if animal == pet:
        
            animals_to_remove.append(animal)

for animal in animals_to_remove:

    animals_in_the_reserve.pop(animal)

print(animals_in_the_reserve)
