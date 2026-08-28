# Estructura de datos para la clase HyBridge
# Acontinuacion aqui nos mostrara la siguiente actividad que debemos de hacer
"""
Crea un programa en Python que organice un registro de viajes usando estructuras de datos complejas. El programa debe:
- Usar una lista de 2 diccionarios, cada uno representando un viaje.
- Cada diccionario debe incluir:
- Llave "destino" (string).
- Llave "actividades" (lista de 2 strings con actividades planeadas).
- Llave "costo" (número entero).
- Pedir al usuario con input():
- Una nueva actividad para el primer viaje.
- Un nuevo costo para el segundo viaje.
- Actualizar el primer viaje agregando la actividad a su lista y reemplazar el costo del segundo viaje.
- Mostrar con print() la lista completa actualizada.
"""

# lista de 2 diccionarios de viajes
viajes = [
    {
        "destino": "Acapulco",
        "actividades": ["Ir a la playa", "Visitar la quebrada"],
        "costo": 884
    },
    {
        "destino": "Ciudad de México",
        "actividades": ["Visitar el museo", "Comer tacos"],
        "costo": 800
    }
]

# pedimos al usuario osea (tu) que ingrese los datos usaremos nuevamente el (input)
new_activity = input("Ingresa una nueva actividad para el primer viaje: ")
new_price = int(input("Ingresa el nuevo costo para el segundo viaje: "))

# actualizamos el primer viaje a la lista
viajes[0]["actividades"].append(new_activity)

# reemplazamos el costo del viaje
viajes[1]["costo"] = new_price

# aqui mostraremos la lista actualizada
print("\n--- Registro de viajes actualizado ---")
print(viajes)
