'''
Created on Apr 20, 2015

@author:  Ricardo Lira y Adriana Devera
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
        
    def testTarifaMuyGrande(self):
        Tar = Tarifa(200000000000000000000,20000000000000000000000000)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-16/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio generar error! Las tarifas son muy grandes")
        
    def testPrimeraTarifaNegativa(self):
        Tar = Tarifa(-100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio generar error! Las tarifas deben ser positivas")
        
    def testSegundaTarifaNegativa(self):
        Tar = Tarifa(100,-200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio generar error! Las tarifas deben ser positivas")
        
    def testAmbasTarifasNegativas(self):
        Tar = Tarifa(-100,-200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-12/16:38","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio generar error! Las tarifas deben ser positivas")
    
    def testMinimoReservaInvalido(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("15-04-10/15:30","%y-%m-%d/%H:%M"), datetime.strptime("15-04-17/15:31","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! La reserva es mayor a 7 dias")
        
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
            self.fail("El metodo debio tirar error! La reserva debe ser mayor de 15 minutos")
            
    def testFechaMuyAntigua(self):
        Tar = Tarifa(100,200)
        tiempo = [datetime.strptime("12-04-9/15:30","%y-%m-%d/%H:%M"), datetime.strptime("12-04-13/15:44","%y-%m-%d/%H:%M")]
        try:
            calcularPrecio(Tar, tiempo)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! La fecha es muy antigua")
   
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