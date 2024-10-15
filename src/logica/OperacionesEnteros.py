# src/logica/OperacionesEnteros.py

from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcularMCD(self):
        if len(self.numeros) < 2:
            raise FaltanParametros("Se requieren al menos dos números para calcular el MCD.")
        elif len(self.numeros) > 1:
            return self._mcd_multiples_numeros()
        else:
            return 0

    def _mcd(self, numero1, numero2):
        """Calcula el MCD de dos números usando el algoritmo de Euclides."""
        while numero2 != 0:
            numero1, numero2 = numero2, numero1 % numero2
        return numero1

    def _mcd_multiples_numeros(self):
        """Calcula el MCD de múltiples números en la lista."""
        for n in self.numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los elementos deben ser enteros.")
        cantidadNumeros = len(self.numeros)
        mcd = self._mcd(self.numeros[0], self.numeros[1])
        for i in range(2, cantidadNumeros):
            mcd = self._mcd(mcd, self.numeros[i])
        return mcd

    def calcularMCM(self):
        if len(self.numeros) < 2:
            raise FaltanParametros("Se requieren al menos dos números para calcular el MCM.")
        elif len(self.numeros) > 1:
            return self._mcm_multiples_numeros()
        else:
            return 0

    def _mcm(self, numero1, numero2):
        """Calcula el MCM de dos números usando la fórmula basada en el MCD."""
        mcd = self._mcd(numero1, numero2)
        return abs(numero1 * numero2) // mcd if mcd != 0 else 0

    def _mcm_multiples_numeros(self):
        """Calcula el MCM de múltiples números en la lista."""
        for n in self.numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los elementos deben ser enteros.")
        cantidadNumeros = len(self.numeros)
        mcm = self._mcm(self.numeros[0], self.numeros[1])
        for i in range(2, cantidadNumeros):
            mcm = self._mcm(mcm, self.numeros[i])
        return mcm
