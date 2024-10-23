class NoSePuedeCalcular(Exception):
    pass
class Promedio:

    def __init__(self,elementos):
        self.__elementos = elementos

    def media(self):
        try:
            if len(self.__elementos) == 0:
                raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía")
            else:
                if len(self.__elementos) == 1:
                    return (self.__elementos[0])

        except  NoSePuedeCalcular:
            return None
