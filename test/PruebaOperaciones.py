import unittest
from src.logica.Promedio import Promedio
from src.logica.DesviacionEstandar import DesviacionEstandar

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

   def test_Promedio_N_elementos_ceros(self):
       elementos = Promedio([0, 0, 0, 0, 0])
       self.assertEqual("Cero", elementos.media())
   def test_Promedio_N_elementos_positivos_y_negativos(self):
       elementos = Promedio([-3, 8, 11, -1, -5])
       self.assertEqual(((8 +11) -(3+1+5))/5, elementos.media())
   def test_Promedio_N_elementos_elementos_no_numericos(self):
       elementos = Promedio(["a","b","c"])
       self.assertEqual("TypeError",elementos.media())
   def test_Desviacion_Estandar_sin_elementos(self):
       elementos=DesviacionEstandar([])
       self.assertIsNone(elementos.desviacionestandar())
   def test_Desviacion_Estandar_un_solo_elemento(self):
       elementos=DesviacionEstandar([8])
       self.assertEqual(0,elementos.desviacionestandar())
   def test_Desviacion_Estandar_dos_elementos(self):
       elementos=DesviacionEstandar([4,6])
       self.assertEqual(1,elementos.desviacionestandar())
   def test_Desviacion_Estandar_N_elementos(self):
       elementos=DesviacionEstandar([5,6,7])
       self.assertEqual((((5-6)**2+(6-6)**2+(7-6)**2)/3)**0.5,elementos.desviacionestandar())
   def test_Desviacion_Estandar_N_elementos_Todos_Ceros(self):
       elementos = DesviacionEstandar([0, 0, 0, 0, 0])
       self.assertEqual("Cero", elementos.desviacionestandar())
   def test_Desviacion_Estandar_N_elementos_positivos_y_negativos(self):
       elementos = DesviacionEstandar([1, -3, 8,])
       self.assertEqual((((1-2)**2+(-3-2)**2+(8-2)**2)/3)**0.5, elementos.desviacionestandar())
   def test_Desviacion_Estandar_N_elementos_que_no_son_numericos(self):
       elementos = DesviacionEstandar(["a","b,","c","d"])
       self.assertEqual("TypeError", elementos.desviacionestandar())