# test/PruebaOperacionesEnteros.py

import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.FaltanParametros import FaltanParametros


class PruebaOperacionesEnteros(unittest.TestCase):

    # Pruebas para calcular MCD
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])
        # Act
        resultadoActual = operacion.calcularMCD()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numeros = [18, 24, 30]
        resultadoEsperado = 6
        operacion = OperacionesEnteros(numeros)
        # Act
        resultadoActual = operacion.calcularMCD()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numeros = [18, 24, 30, 42]
        resultadoEsperado = 6
        operacion = OperacionesEnteros(numeros)
        # Act
        resultadoActual = operacion.calcularMCD()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numeros = [18]
        operacion = OperacionesEnteros(numeros)
        # Assert
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_unaCadena_lanzaExcepcion(self):
        # Arrange
        numeros = ["18a", 13]
        operacion = OperacionesEnteros(numeros)
        # Assert
        with self.assertRaises(ValueError):
            operacion.calcularMCD()

    # Pruebas para calcular MCM
    def test_MCM_dosNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 4
        numero2 = 6
        resultadoEsperado = 12
        operacion = OperacionesEnteros([numero1, numero2])
        # Act
        resultadoActual = operacion.calcularMCM()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_tresNumerosPositivos_retornaMCM(self):
        # Arrange
        numeros = [4, 6, 8]
        resultadoEsperado = 24
        operacion = OperacionesEnteros(numeros)
        # Act
        resultadoActual = operacion.calcularMCM()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_cuatroNumerosPositivos_retornaMCM(self):
        # Arrange
        numeros = [4, 6, 8, 10]
        resultadoEsperado = 120
        operacion = OperacionesEnteros(numeros)
        # Act
        resultadoActual = operacion.calcularMCM()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numeros = [18]
        operacion = OperacionesEnteros(numeros)
        # Assert
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCM()

    def test_MCM_unaCadena_lanzaExcepcion(self):
        # Arrange
        numeros = ["18a", 13]
        operacion = OperacionesEnteros(numeros)
        # Assert
        with self.assertRaises(ValueError):
            operacion.calcularMCM()


if __name__ == '__main__':
    unittest.main()
