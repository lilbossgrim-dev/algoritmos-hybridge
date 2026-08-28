# Esto es una receta de cocina para la clase de HyBridge
# Para poder guardar en un solo comentario sin necesidad de usar el # en cada linea puedes hacerlo asi usan 3 de esto entre comillas " como esta en el ejemplo
# Acontinuacion se mostrara un ejemplo que nos otorga la clase:
"""
¡Bienvenid@ al recetario Python!
Nombre de la receta: Sandwich de jamón y chile
Ingresa los ingredientes de la receta: pan, mayonesa, mostaza, jamón, chiles
Paso 1: Untar mayonesa en un pan y mostaza en el otro
Paso 2: Colocar jamon y chiles en cualquier de los dos panes
Paso 3: Cerrar el sandwich

¡Receta guardada!

============================================================
Sandwich de jamón y chile
Ingredientes: pan, mayonesa, mostaza, jamón, chiles
Paso 1: Untar mayonesa en un pan y mostaza en el otro
Paso 2: Colocar jamon y chiles en cualquier de los dos panes
Paso 3: Cerrar el sandwich
==============================================================
"""

# Usaremos la misma receta de la clase empezaremos usando solo 2 metodos en la receta el print y input
# Antes de comenzar debemos de saber como funciona cada uno de los dos
# input sirve para detener el programa y esperar a que el usuario escriba algo
# print sirve para imprimir los textos y variables

print("¡Bienvenid@ al recetario Python!")

name = input("Nombre de la receta: ")
Ingredients = input("Ingresa los ingredientes de la receta: ")
step1 = input("Paso 1: ")
step2 = input("Paso 2: ")
step3 = input("Paso 3: ")

# Mostramos el resultado final
print("\n¡Receta guardada!")
print("=" * 60)
print(name)
print(f"Ingredientes: {Ingredients}")
print(f"Paso 1: {step1}")
print(f"Paso 2: {step2}")
print(f"Paso 3: {step3}")
print("=" * 60)
