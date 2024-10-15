class Cliente:
    def __init__(self, nombre, apellido, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion

    def get_data(self):
        return f'{self.nombre} - {self.apellido} - {self.dni} - {self.direccion})'

    