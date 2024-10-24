class NoSePuedeCalcular(Exception):
    pass

class DesviacionEstandar:
    def __init__(self, elementos):
        self.__elementos = elementos
    def desviacionestandar(self):
        try:
            if len(self.__elementos) == 0:
                raise NoSePuedeCalcular("No se puede calcular la desviacion estandar de una lista vacía")
            if len(self.__elementos) == 1:
                return 0
        except NoSePuedeCalcular:
            return None
