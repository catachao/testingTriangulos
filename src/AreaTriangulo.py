import math
class AreaTriangulo:

    def calcular_area_lados(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Todos los lados deben ser mayores que cero.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("La suma de dos lados debe ser mayor que el tercer lado.")

        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

