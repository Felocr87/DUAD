# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`



hotel_information = {
    "Hotel" : "Manzanillo",
    "Class" : "3 stars",
    "Rooms" : {
        "Room 1" : {
            "Number" : "01",
            "Level" : "01",
            "Price per night (USD)" : 80
        },
        "Room 2" : {
            "Number" : "02",
            "Level" : "01",
            "Price per night (USD)" : 80
        },
        "Room 3" : {
            "Number" : "03",
            "Level" : "02",
            "Price per night (USD)" : 90
        },
        "Room 4" : {
            "Number" : "04",
            "Level" : "03",
            "Price per night (USD)" : 100
        },
        },
}

print (hotel_information)