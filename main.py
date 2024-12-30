import random

# Diccionario para almacenar el inventario de vata
inventario = {
    "vata_estéril": 100,
    "vata_no_estéril": 150,
    "algodón": 50,
    "gasas": 80
}

# Lista de precios por unidad
precios = {
    "vata_estéril": 2.5,
    "vata_no_estéril": 2.0,
    "algodón": 1.5,
    "gasas": 3.0
}

def mostrar_catalogo():
    print("Catálogo de productos:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades disponibles (${precios[producto]} cada una)")

def agregar_al_carrito():
    global carrito
    mostrar_catalogo()
    producto = input("Ingrese el producto que desea agregar: ")
    cantidad = int(input("Ingrese la cantidad: "))

    if producto in inventario and cantidad <= inventario[producto]:
        inventario[producto] -= cantidad
        carrito.append((producto, cantidad))
        print(f"{cantidad} unidades de {producto} agregadas al carrito.")
    else:
        print("Producto no encontrado o cantidad no disponible.")

def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Contenido del carrito:")
        total = 0
        for producto, cantidad in carrito:
            precio_unitario = precios[producto]
            subtotal = cantidad * precio_unitario
            print(f"- {cantidad} x {producto} = ${subtotal:.2f}")
            total += subtotal
        print(f"Total a pagar: ${total:.2f}")

def finalizar_compra():
    global carrito
    if not carrito:
        print("El carrito está vacío.")
        return

    ver_carrito()
    print("Gracias por su compra. ¡Vuelva pronto!")
    carrito = []

def main():
    carrito = []  # Inicializamos el carrito en cada ejecución
    while True:
        print("\n--- Menú ---")
        print("1. Ver catálogo")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            finalizar_compra()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()