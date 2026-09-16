import math
from multimethod import multimethod

class Vector:

    @multimethod
    def __init__(self):
        self.__a1 = 0.0
        self.__a2 = 0.0
        self.__a3 = 0.0

    @multimethod
    def __init__(self, a1, a2, a3):
        self.__a1 = float(a1)
        self.__a2 = float(a2)
        self.__a3 = float(a3)

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def longitud(self):
        return math.sqrt(self.__a1**2 + self.__a2**2 + self.__a3**2)

    def __abs__(self):
        return self.longitud()

    def __add__(self, b: "Vector"):
        return Vector(
            self.__a1 + b.get_a1(), self.__a2 + b.get_a2(), self.__a3 + b.get_a3()
        )

    @multimethod
    def __mul__(self, r):
        return Vector(self.__a1 * r, self.__a2 * r, self.__a3 * r)

    @multimethod
    def __mul__(self, b: "Vector"):
        return (
            self.__a1 * b.get_a1() + self.__a2 * b.get_a2() + self.__a3 * b.get_a3()
        )

    def __rmul__(self, r):
        return self.__mul__(r)

    def normal(self):
        m = self.longitud()
        if m == 0:
            print("Error: No se puede normalizar un vector nulo.")
            return None
        return Vector(self.__a1 / m, self.__a2 / m, self.__a3 / m)

    def producto_vectorial(self, b: "Vector"):
        c1 = self.__a2 * b.get_a3() - self.__a3 * b.get_a2()
        c2 = self.__a3 * b.get_a1() - self.__a1 * b.get_a3()
        c3 = self.__a1 * b.get_a2() - self.__a2 * b.get_a1()
        return Vector(c1, c2, c3)

    def __str__(self):
        return f"({self.__a1:.2f}, {self.__a2:.2f}, {self.__a3:.2f})"


if __name__ == "__main__":
    a = Vector(2, 3, 4)
    b = Vector(1, -2, 2)

    print(f"Vector a: {a}")
    print(f"Vector b: {b}\n")

    c = a + b
    print(f"a) Suma (a + b): {c}")

    r = 3
    print(f"b) Escalar (3 * a): {3 * a}")

    print(f"c) Longitud |a|: {abs(a):.2f}")

    print(f"d) Normal de a: {a.normal()}")

    prod_escalar = a * b
    print(f"e) Producto escalar (a . b): {prod_escalar}")

    prod_vectorial = a.producto_vectorial(b)
    print(f"f) Producto vectorial (a x b): {prod_vectorial}")