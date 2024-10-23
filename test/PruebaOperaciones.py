import unittest
from src.logica.Promedio import Promedio

class PruebaOperaciones(unittest.TestCase):

   def test_Promedio_vacio_retornaNone(self):
      elementos =Promedio([])
      self.assertIsNone(elementos.media())
   def test_Promedio_un_solo_Elemento(self):
      elementos = Promedio([6])
      self.assertEqual(elementos.media(), 6)