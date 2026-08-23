# Una calculadora que hace descuentos para una tienda en linea para la clase Hybridge

# La tienda tiene las siguientes reglas para otorgar descuentos:

# Si el usuario es miembro premium y su compra es mayor a $500 y recibe un 20% de descuento
# Si el usuario no es miembro premium pero su compra es mayor a $1,000 y recibe un 10% de descuento
# Si el usuario es estudiante y su compra es mayor a $200 y recibe un 15% de descuento 
# Si no cumple ninguna de estas condiciones y no recibe descuento

class Calculadora:

    def __init__(self, es_premium, es_estudiante, cantidad, usuario):
        self.es_premium = es_premium
        self.es_estudiante = es_estudiante
        self.cantidad = cantidad
        self.usuario = usuario

        if self.es_premium and self.cantidad > 500:
            self.porcentaje_descuento = 0.20
            self.mensaje = (
                "SUPEEEEEEEEEEER, eres miembro premium :) y tu compra es mayor a $500 (20% de descuento)"
            )
        elif not self.es_premium and self.cantidad > 1000:
            self.porcentaje_descuento = 0.10
            self.mensaje = (
                "Ups, no eres miembro premium :( pero tu compra es mayor a $1,000 (10% de descuento)"
            )
        elif self.es_estudiante and self.cantidad > 200:
            self.porcentaje_descuento = 0.15
            self.mensaje = (
                "Eres estudiante y tu compra es mayor a $200 (15% de descuento)"
            )
        else:
            self.porcentaje_descuento = 0.0
            self.mensaje = "No cumples con las condiciones para recibir un descuento"

        # calcular el monto final del descuento
        self.monto_descuento = self.cantidad * self.porcentaje_descuento

    def mostrar_resultado(self):
        print(f"Usuario: {self.usuario}")
        print(f"Mensaje: {self.mensaje}")
        print(f"Cantidad original: ${self.cantidad}")
        print(f"Descuento obtenido: ${self.monto_descuento}")
        print(
            f"Total a pagar: ${self.cantidad - self.monto_descuento}\n"
            + "-" * 40
        )

# miembro premium mayor a 500
compra1 = Calculadora(
    es_premium=True, es_estudiante=False, cantidad=600, usuario="premium"
)
compra1.mostrar_resultado()

# estudiante mayor a 200
compra2 = Calculadora(
    es_premium=False, es_estudiante=True, cantidad=300, usuario="estudiante"
)
compra2.mostrar_resultado()

# estudiante no premium pero mayor a $1,000
compra3 = Calculadora(
    es_premium=False, es_estudiante=False, cantidad=1100, usuario="no premium"
)
compra3.mostrar_resultado()
