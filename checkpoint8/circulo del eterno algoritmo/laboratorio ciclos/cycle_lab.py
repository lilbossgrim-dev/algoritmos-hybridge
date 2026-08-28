# Crearemos un programa con validacion de usario y contraseña usando ciclos de for y while para la clase HyBridge
# Acontinuacion aqui se muestra la actividad que debemos de realizar

"""
Implementa un programa que valide un usuario y contraseña usando ciclos for y while. El usuario tiene un máximo de 3 intentos para ingresar correctamente sus credenciales.

Requisitos
- Tienes una lista de diccionarios llamada usuarios.
- Cada diccionario contiene dos llaves: "user" y "password".
- Utiliza un ciclo while para permitir al usuario un máximo de 3 intentos para iniciar sesión.
- Dentro del ciclo while, usa un ciclo for para recorrer la lista y validar el usuario y contraseña.
- Si las credenciales son correctas, muestra un mensaje de bienvenida y termina el programa.
- Si se agotan los 3 intentos sin éxito, muestra un mensaje indicando que la cuenta está bloqueada.
"""

usuarios = [
    {"user": "lilbossdev", "password": "777"},
    {"user": "ceo", "password": "ceo777"}
]

intentos = 3

while intentos > 0:
    ingreso_usuario = input("Ingresa tu usuario: ")
    ingreso_password = input("Ingresa tu contraseña: ")

    credenciales_validas = False

    # aqui reecorremos la lista de diccionarios
    for u in usuarios:
        if u["user"] == ingreso_usuario and u["password"] == ingreso_password:
            credenciales_validas = True
            break
# aqui validamos que las credenciales sean validad para darles acceso
    if credenciales_validas:
        print("¡Bienvenido! Inicio de sesión exitoso.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Datos incorrectos. Te quedan {intentos} intentos.")
        else:
            print("Cuenta bloqueada. Has agotado los 3 intentos.")
