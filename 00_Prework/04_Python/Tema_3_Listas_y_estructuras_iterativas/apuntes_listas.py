# -- Listas --

coches = ["BMW", "Mercedes", "Audi", "Ferrari"] # Las listas son mutables, lo que significa que podemos modificar su contenido después de haberlas creado.
numeros = [1, 2, 3, 4, 5] # Las listas pueden contener cualquier tipo de dato, incluso mezclados
cosas = ["Hola", 42, True, 3.14] # Las listas pueden contener otras listas, lo que se conoce como listas anidadas

print(coches) # Imprime la lista completa
print(coches[0]) # Imprime el primer elemento de la lista (BMW)
print(coches[1]) # Imprime el segundo elemento de la lista (Mercedes)
print(numeros) # Imprime la lista completa
print(cosas) # Imprime la lista completa


# append() -> Agrega un elemento al final de la lista.
print("Antes de agregar un nuevo coche: ", coches)
coches.append("Porsche") # Agrega "Porsche" al final de la lista de coches
print("Después de agregar un nuevo coche: ", coches)

# insert() -> Agrega un elemento en una posición específica de la lista.
print("Antes de insertar un nuevo coche: ", coches)
coches.insert(2, "Lamborghini") # Inserta "Lamborghini" en la posición 2 de la lista de coches
print("Después de insertar un nuevo coche: ", coches)