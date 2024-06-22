class Paquete:
    __numeroEnvio: int
    __peso: float
    __nombreDestinatario: str
    __direccionDestinatario: str
    __entregado: bool
    __observaciones: str
    __repartidor: object
    __sucursal: object
    __transporte: object
    def __init__(self, numeroEnvio, peso, nombreDestinatario, direccionDestinatario, entregado, observaciones):
        self.__numeroEnvio = numeroEnvio
        self.__peso = peso
        self.__nombreDestinatario = nombreDestinatario
        self.__direccionDestinatario = direccionDestinatario
        self.__entregado = entregado
        self.__observaciones = observaciones
        self.__repartidor = None
        self.__sucursal = None
        self.__transporte = None

    def get_numeroEnvio(self):
        return self.__numeroEnvio

    def set_numeroEnvio(self, numeroEnvio):
        self.__numeroEnvio = numeroEnvio

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_nombreDestinatario(self):
        return self.__nombreDestinatario

    def set_nombreDestinatario(self, nombreDestinatario):
        self.__nombreDestinatario = nombreDestinatario

    def get_direccionDestinatario(self):
        return self.__direccionDestinatario

    def set_direccionDestinatario(self, direccionDestinatario):
        self.__direccionDestinatario = direccionDestinatario

    def get_entregado(self):
        return self.__entregado

    def set_entregado(self, entregado):
        self.__entregado = entregado

    def get_observaciones(self):
        return self.__observaciones

    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones

    def get_repartidor(self):
        return self.__repartidor

    def set_repartidor(self, repartidor):
        self.__repartidor = repartidor

    def get_sucursal(self):
        return self.__sucursal

    def set_sucursal(self, sucursal):
        self.__sucursal = sucursal

    def get_transporte(self):
        return self.__transporte

    def set_transporte(self, transporte):
        self.__transporte = transporte

    def __repr__(self):
        return f'<Paquete {self.__numeroEnvio}>'