# Crearemos un programa que organice los gatos de un viaje para la clase HyBridge
# Acontinuacion esta es la actividad que realizaremos
"""
Crea un programa en Python que calcule y organice los gastos de un viaje usando al menos tres funciones. El programa debe:
- Definir y usar estas funciones:
- calcular_transporte(distancia): Recibe la distancia en kilómetros (número), calcula el costo de transporte (distancia * 5 pesos por km), y devuelve el costo.
- calcular_comida(dias, presupuesto_diario=50): Recibe los días del viaje (número) y un presupuesto diario opcional (en pesos), calcula el costo total de comida (días * presupuesto_diario), y devuelve el costo.
- mostrar_resumen(destino, costo_transporte, costo_comida): Recibe el destino (string) y los costos calculados, calcula el costo total (transporte + comida), y devuelve un mensaje con el resumen.

Pedir al usuario con input():
- El destino del viaje (string).
- La distancia en kilómetros (número).
- Los días del viaje (número).
- Usar las funciones para calcular los costos y mostrar el resumen.
- Mostrar el mensaje final con print().
"""
# usaremos 4 metodos el def para definir una clase, el input para que el usuario pueda escribir, el int para convertir el texto o numero decimal o entero y el float para convertir numero decimales

# aqui definimos las 3 clases
def calcular_transporte(distancia):
    return distancia * 5

def calcular_comida(dias, presupuesto_diario=50):
    return dias * presupuesto_diario

def mostrar_resumen(destino, costo_transporte, costo_comida):
    costo_total = costo_transporte + costo_comida
    mensaje = f"Destino: {destino}\nCosto de transporte: ${costo_transporte}\nCosto de comida: ${costo_comida}\nCosto total del viaje: ${costo_total}"
    return mensaje

# aqui pedimos lo datos osea (tu)
destino_usuario = input("Ingresa el destino del viaje: ")
distancia_usuario = float(input("Ingresa la distancia en kilómetros: "))
dias_usuario = int(input("Ingresa los días del viaje: "))

# aqui calculamos los costos
costo_t = calcular_transporte(distancia_usuario)
costo_c = calcular_comida(dias_usuario)

# aqui obtenemos el resumen
resumen_final = mostrar_resumen(destino_usuario, costo_t, costo_c)

# mostrar el mensaje
print("\n--- Resumen de gastos del viaje ---")
print(resumen_final)
