class NoSePuedeCalcular(Exception):
    pass

class DesviacionEstandar:
    def __init__(self, elementos):
        self.__elementos = elementos
    def desviacionestandar(self):
        try:
            if len(self.__elementos) == 0:
                raise NoSePuedeCalcular("No se puede calcular la desviacion estandar de una lista vacía")

        except NoSePuedeCalcular:
            return None
