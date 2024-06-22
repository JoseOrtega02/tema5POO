class Sucursal:
    def __init__(self, numero, provincia, localidad, direccion):
        self.__numero = numero
        self.__provincia = provincia
        self.__localidad = localidad
        self.__direccion = direccion
        self.__paquetes = []
        self.__repartidores = []

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_provincia(self):
        return self.__provincia

    def set_provincia(self, provincia):
        self.__provincia = provincia

    def get_localidad(self):
        return self.__localidad

    def set_localidad(self, localidad):
        self.__localidad = localidad

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_paquetes(self):
        return self.__paquetes

    def set_paquetes(self, paquetes):
        self.__paquetes = paquetes

    def get_repartidores(self):
        return self.__repartidores

    def set_repartidores(self, repartidores):
        self.__repartidores = repartidores

    def __repr__(self):
        return f'<Sucursal {self.__numero}>'
