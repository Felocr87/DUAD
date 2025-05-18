# 4. Cree un programa que elimine todos los números impares de una lista.



my_list = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    11,
    13,
    15,
    10,
    12,
    14,
	16,
	18,
	20,
]



for index in range(len(my_list)-1,0,-1):
	number = my_list[index]
	if number % 2 == 1:
	    del my_list[index]
    
    

print(my_list)
