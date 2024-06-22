class Repartidor:
    def __init__(self, numero, nombre, dni):
        self.__numero = numero
        self.__nombre = nombre
        self.__dni = dni
        self.__paquetes = []

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_paquetes(self):
        return self.__paquetes

    def set_paquetes(self, paquetes):
        self.__paquetes = paquetes

    def __repr__(self):
        return f'<Repartidor {self.__nombre}>'
