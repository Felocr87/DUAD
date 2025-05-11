import json

# 1. Leer el archivo JSON
with open('datos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

print(datos)


# # 2. Agregar nueva información
# nuevo_usuario = {"nombre": "Carlos", "edad": 28}
# datos["usuarios"].append(nuevo_usuario)

# # 3. Guardar los datos nuevamente en el archivo JSON
# with open('datos.json', 'w', encoding='utf-8') as archivo:
#     json.dump(datos, archivo, indent=4, ensure_ascii=False)

# print("Usuario agregado exitosamente.")
