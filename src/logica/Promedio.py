class NoSePuedeCalcular(Exception):
    pass
class Promedio:

    def __init__(self,elementos):
        self.elementos = elementos

    def media(self):
        try:
            pass
        except  NoSePuedeCalcular:
            return None
