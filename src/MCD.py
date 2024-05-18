class MCD:
    def maximoComunDivisor(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
