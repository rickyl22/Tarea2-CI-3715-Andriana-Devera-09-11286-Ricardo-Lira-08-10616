'''
Created on Apr 20, 2015

@author: Ricardo Lira y Adriana Devera
'''
import unittest
from calcularPrecio import *
from datetime import datetime
from test.test_deque import fail

class calcularPrecioTest(unittest.TestCase):

    def testMaximoDiasFinDeSemana(self):
        Tar = Tarifa(1,2)
        tiempo = [datetime.strptime("15-04-25/00:00","%y-%m-%d/%H:%M"), datetime.strptime("15-04-27/00:00","%y-%m-%d/%H:%M")]
        self.assertEqual(calcularPrecio(Tar,tiempo), 96, "Error en calculo de Tarifa")
        
    def testMaximoDiasSemana(self):
        Tar = Tarifa(1,2)
        tiempo = [datetime.strptime("15-04-20/00:00","%y-%m-%d/%H:%M"), datetime.strptime("15-04-25/00:00","%y-%m-%d/%H:%M")]
        self.assertEqual(calcularPrecio(Tar,tiempo), 120, "Error en calculo de Tarifa")
        
    def testMinimaTarifaValida(self):
        Tar = Tarifa(0,0)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        self.assertEqual(calcularPrecio(Tar,tiempo), 0, "Error en calculo de Tarifa")
        
    def testTarifaNegativa(self):
        Tar = Tarifa(-100,-200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
            fail("El metodo debio generar error!")
        except Exception:
            pass
    
    def testMinimoReservaInvalido(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-17/15:31","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error!")
        
    def testMaximoReservaValido(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-17/15:30","%y-%m-%d/%H:%M")]        
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            self.fail("El metodo debio ejecutarse!")
        else:
            pass
        
        
         
    def testMinimoReservaValido(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-10/15:45","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            self.fail("El metodo debio ejecutarse!")
        else:
            pass
        
    def testMaximoReservaInvalido(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-10/15:44","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error!")
   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()