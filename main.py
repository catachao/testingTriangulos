import unittest
from src.MCD import MCD
from src.Triangulo import AreaTriangulo

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

class TestTriangulo(unittest.TestCase):
    def es_triangulo(self):
        area_triangulo = AreaTriangulo()
        test_cases = [
            (3, 4, 5, 6),
            (6, 8, 10, 24),
            (7, 10, 5, 16.24807680927192),
        ]

        for a, b, c, expected in test_cases:
            with self.subTest(a=a, b=b, c=c, expected=expected):
                self.assertAlmostEqual(expected, area_triangulo.calcular_area_lados(a, b, c), places=5)

    def no_es_triangulo(self):
        area_triangulo = AreaTriangulo()
        invalid_test_cases = [
            (-3, 4, 5),
            (3, -4, 5),
            (3, 4, -5),
            (1, 1, 3),
            (1, 2, 4),
            (2, 2, 5),
        ]

        for a, b, c in invalid_test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    area_triangulo.calcular_area_lados(a, b, c)

if __name__ == '__main__':
    unittest.main()
