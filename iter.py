i = 0
j = 0
while i < 10:
    while j < 11:
        print(i, j)
        j += 1
        
        if j > 3:
            break
    i += 1
    j = 0



frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
next(iterador)

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    ...

for pais in estudiantes.keys():
    ...

for numero_de_estudiantes in estudiantes.values():
    ...

for pais, numero_de_estudiantes in estudiantes.items():
    ...

    