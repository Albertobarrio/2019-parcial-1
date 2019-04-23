import unittest

from interfaz import interfaz

class TestInterfazHexadecimal(unittest.TestCase):
    def test_interfaz_hexadecmal_hola(self):
        result = interfaz("HOLA")
        self.assertEqual(result,'ERROR:Debe ingresar un numero entero')
        
if __name__ == '__main__':
    unittest.main()