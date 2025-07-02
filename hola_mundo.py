# 1. Imprime "Hola, mundo"

print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Nathalia"

print( "Hola,", nombre) # con una coma

print( "Hola, " + nombre) # con un +	(no te olvides de un espacio en blanco" ) # con un +

# 3. Imprimir "Hola 970!" con el número en una variable

numero = 970

print("Hola", numero, "!") # con una coma

print("Hola, " + str(numero) + "!") # con un + (no te olvides de convertir el número a cadena)

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "guacamole"

comida2 = "arepas"

print("¡Me encanta comer {} y {}!".format(comida1, comida2) ) # con una coma

print(f"¡Me encanta comer {comida1} y {comida2}!") # con .format()