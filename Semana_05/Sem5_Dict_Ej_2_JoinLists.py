# 1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
# usando una para sus keys, y la otra para sus values.


list_a = [
    "7am",
    "10am",
    "12md",
    "4pm",
    "7pm",
]


list_b = [
    "Breakfast",
    "Snack",
    "Lunch",
    "Coffee break",
    "Dinner",
]

meal_times = {
    
}

counter = 0

for index in list_a:
   
    meal_times [f"{index}"] = f"{list_b[counter]}"
    counter += 1

print(meal_times)
