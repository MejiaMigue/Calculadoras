import unittest

# Función de suma
def suma(num1, num2):
    return num1 + num2

# Función de resta
def resta(num1, num2):
    return num1 - num2

# Función de multiplicación
def multiplicacion(num1, num2):
    return num1 * num2

# Función de división
def division(num1, num2):
    if num2 == 0:
        return "Error: división por cero"
    else:
        return num1 / num2

# Clase de pruebas para la calculadora
class TestCalculadora(unittest.TestCase):
    
    # Prueba para la función de suma
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-3, -5), -8)
        self.assertEqual(suma(3, -5), -2)
        self.assertEqual(suma(0, 5), 5)
        self.assertEqual(suma(0, -5), -5)
        self.assertEqual(suma(0, 0), 0)

    # Prueba para la función de resta
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(5, -3), 8)
        self.assertEqual(resta(-5, 3), -8)
        self.assertEqual(resta(-5, -3), -2)
        self.assertEqual(resta(0, 5), -5)
        self.assertEqual(resta(0, -5), 5)
        self.assertEqual(resta(0, 0), 0)

    # Prueba para la función de multiplicación
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 5), 15)
        self.assertEqual(multiplicacion(-3, -5), 15)
        self.assertEqual(multiplicacion(3, -5), -15)
        self.assertEqual(multiplicacion(0, 5), 0)
        self.assertEqual(multiplicacion(0, -5), 0)
        self.assertEqual(multiplicacion(0, 0), 0)

    # Prueba para la función de división
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(10, -2), -5)
        self.assertEqual(division(-10, -2), 5)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(0, -5), 0)
        self.assertEqual(division(0, 0), "Error: división por cero")

if __name__ == '__main__':
    unittest.main()