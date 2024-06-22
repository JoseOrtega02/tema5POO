from datetime import datetime

class Transporte:
    __numeroTransporte:int
    __fechaHoraLlegada:datetime
    __fechaHoraSalida:datetime
    __paquetes:object
    def __init__(self, numeroTransporte, fechaHoraSalida, fechaHoraLlegada):
        self.__numeroTransporte = numeroTransporte
        self.__fechaHoraSalida = fechaHoraSalida
        self.__fechaHoraLlegada = fechaHoraLlegada
        self.__paquetes = []

    def get_numeroTransporte(self):
        return self.__numeroTransporte

    def set_numeroTransporte(self, numeroTransporte):
        self.__numeroTransporte = numeroTransporte

    def get_fechaHoraSalida(self):
        return self.__fechaHoraSalida

    def set_fechaHoraSalida(self, fechaHoraSalida):
        self.__fechaHoraSalida = fechaHoraSalida

    def get_fechaHoraLlegada(self):
        return self.__fechaHoraLlegada

    def set_fechaHoraLlegada(self, fechaHoraLlegada):
        self.__fechaHoraLlegada = fechaHoraLlegada

    def get_paquetes(self):
        return self.__paquetes

    def set_paquetes(self, paquetes):
        self.__paquetes = paquetes

    def __repr__(self):
        return f'<Transporte {self.__numeroTransporte}>'
