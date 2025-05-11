# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def this_is_the_first_function ():
    print ("simple things!")


def this_is_the_second_function ():
    print ("I like...")
    this_is_the_first_function()


this_is_the_second_function()
    