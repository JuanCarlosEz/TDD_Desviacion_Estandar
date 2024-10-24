import unittest
from src.logica.Promedio import Promedio

class PruebaOperaciones(unittest.TestCase):

   def test_Promedio_vacio_retornaNone(self):
      elementos =Promedio([])
      self.assertIsNone(elementos.media())
   def test_Promedio_unElemento(self):
        elementos = Promedio([6])
        self.assertEqual(elementos.media(), 6)
   def test_Promedio_de_dos_elementos(self):
        elementos = Promedio([2,6])
        self.assertEqual(elementos.media(), 4)
   def test_Promedio_N_elementos(self):
        elementos=Promedio([4,6,8,10,12])
        self.assertEqual((4+6+8+10+12)/5,elementos.media())