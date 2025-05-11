# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.


birth_month = "January"


def birthday ():
    birth_date = 12
    print (f"My birthday is: {birth_month} {birth_date}")


birthday()

print (f"The best day for the world history is: {birth_month} {birth_date}")

# Esto genera error porque se está intentando utilizar la variable birth_date fuera de la función birthday (scope local). 
# Sin embargo, la variable birth_month sí pudo utilizarse dentro de la función birthday porque su scope es global.