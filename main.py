from Clientes import Cliente

def main():
    nombre = input("INGRESE NOMBRE CLIENTE: ")
    apellido = input("INGRESE APELLIDO CLIENTE: ")
    dni = input("INGRESE DNI CLIENTE: ")
    direccion = input("INGRESE DIRECCION CLIENTE: ")
    cliente_1 = Cliente(nombre, apellido, dni, direccion)
    print(cliente_1.get_data())

if __name__ == '__main__':
    main()