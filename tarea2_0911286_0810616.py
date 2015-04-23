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

    ##Se procede a realizar caso de prueba con malicia.
    def testCalcularPrecio1(self):
        Prec= Tarifa(200,500)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-10/15:40","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Prec, tiempo)
            fail("Se debe generar un error de calculo de tarifa")
        except Exception:
            pass 
   
    def testTarifaFlotante(self):
        Tar = Tarifa(2.33333333333,3.5555555)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-16/16:38","%y-%m-%d/%H:%M")]
        calcularPrecio(Tar,tiempo)
        pass

    def testTarifaCaracter(self):
        Tar = Tarifa("a","b")
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-16/16:38","%y-%m-%d/%H:%M")]
        calcularPrecio(Tar,tiempo)
        pass
    
    def testFechaFinalAnterior(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-5/15:30","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! El fin de la reserva debe ser posterior al inicio de la reserva")
            
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()