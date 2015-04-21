'''
Created on Apr 20, 2015

@author: Ricardo Lira y Adriana Devera
'''
import unittest
from calcularPrecio import *
from datetime import datetime
from test.test_deque import fail

class calcularPrecioTest(unittest.TestCase):


    def testTarifaNegativa(self):
        Tar = Tarifa(-100,-200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
            fail("El metodo debio generar error!")
        except Exception:
            pass
        
    def testMaximoReserva(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-25/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
            fail("El metodo debio generar error!")
        except Exception:
            pass
        
         
    def testMinimoReserva(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-10/15:40","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
            fail("El metodo debio generar error!")
        except Exception:
            pass
    ##Se procede a realizar un caso de prueba con malicia.
    def testCalcularPrecioMal1(self):
        Prec= TarifaMal(200,500)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-10/15:40","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Prec, tiempo)
            fail("Se debe generar un error de calculo de tarifa")
            pass 
   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()