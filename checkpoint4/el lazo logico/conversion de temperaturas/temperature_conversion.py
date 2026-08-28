# Conversion de temperaturas para la clase HyBridge
# Crea un programa que convierta una temperatura de grados Celsius a Fahrenheit y determine si es un día caluroso. La fórmula para convertir Celsius a Fahrenheit es:
# F = (C * 9/5) + 32
# Ejemplo de la clase
"""
Ingresa la temperatura en Celsius: 30
Temperatura en Fahrenheit: 86.0
¿Es un día caluroso? True
"""

# Nos pide la clase que creemos uno
"""
Crea un programa que convierta una temperatura de grados Celsius a Fahrenheit y determine si es un día caluroso. 
Un día se considera caluroso si la temperatura en Fahrenheit es mayor o igual a 86°F. 1) 
Pide al usuario que ingrese una temperatura en grados Celsius usando input. 2) Convierte la temperatura a Fahrenheit usando operaciones aritméticas. 3) 
Usa un operador de comparación para determinar si es un día caluroso (True o False). 4) Muestra la temperatura en Fahrenheit y si es un día caluroso o no.
"""

# aqui pedimos al usuario (osea tu) que ingrese la temperatura
celsius = float(input("Ingresa la temperatura en Celsius: "))

# aqui convertimos la temperatura fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# aqui usamos el numero de comparacion que nos indica que es 86 para ver si es caluroso
is_caluroso = fahrenheit > 86

# aqui muestra los resultados
print(f"La temperatura en Fahrenheit es: {fahrenheit}")
print(f"Hoy es un dia caluroso?: {is_caluroso}") #True
#podemos usar tambien este pero solo llevara un numero flotante osea (float) por que es decimal
#print(f"Hoy es un dia caluroso?: {celsius}")
