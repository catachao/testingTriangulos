import unittest
from src.MCD import MCD
from src.AreaTriangulo import AreaTriangulo

class TestMCD(unittest.TestCase):
    def test_maximo_comun_divisor(self):
        mcd = MCD()
        test_cases = [
            (48, 18, 6),
            (56, 98, 14),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(expected, mcd.maximoComunDivisor(a, b))

class TestAreaTriangulo(unittest.TestCase):
    def test_calculo_area(self):
        area_triangulo = AreaTriangulo()
        test_cases = [
            (10, 5, 25),
            (7, 3, 10.5),
            (8, 6, 24),
        ]

        for base, altura, expected in test_cases:
            with self.subTest(base=base, altura=altura, expected=expected):
                self.assertEqual(expected, area_triangulo.calcular_area(base, altura))

    def test_calculo_area_valores_invalidos(self):
        area_triangulo = AreaTriangulo()
        invalid_test_cases = [
            (-10, 5),
            (10, -5),
            (0, 5),
            (10, 0),
        ]

        for base, altura in invalid_test_cases:
            with self.subTest(base=base, altura=altura):
                with self.assertRaises(ValueError):
                    area_triangulo.calcular_area(base, altura)

if __name__ == '__main__':
    unittest.main()
