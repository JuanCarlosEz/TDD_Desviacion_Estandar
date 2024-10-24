class NoSePuedeCalcular(Exception):
    pass


class Promedio:

    def __init__(self, elementos):
        self.__elementos = elementos

    def media(self):
        try:
            if not self.__elementos:
                raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía")

            if not all(isinstance(x, (int, float)) for x in self.__elementos):
                raise TypeError("Todos los elementos deben ser números")

            if all(x == 0 for x in self.__elementos):
                return "Cero"

            if len(self.__elementos) == 1:
                return self.__elementos[0]
            if len(self.__elementos) >=2:
                suma_positivos = sum(x for x in self.__elementos if x > 0)
                suma_negativos = sum(abs(x) for x in self.__elementos if x < 0)
                return (suma_positivos - suma_negativos) / len(self.__elementos)

        except NoSePuedeCalcular:
            return None
        except TypeError:
            return "TypeError"