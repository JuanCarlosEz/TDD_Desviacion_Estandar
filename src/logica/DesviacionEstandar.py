from src.logica.Promedio import Promedio
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
            if len(self.__elementos) == 2:
                media=Promedio(self.__elementos).media()
                x1, x2 = self.__elementos
                return (((x1 - media) ** 2 + (x2 - media) ** 2)/ 2 ) ** 0.5
            if len(self.__elementos) > 2:
                media = Promedio(self.__elementos).media()
                suma_cuadrados=sum((x - media) ** 2 for x in self.__elementos)
                return (suma_cuadrados / len(self.__elementos)) ** 0.5
        except NoSePuedeCalcular:
            return None
