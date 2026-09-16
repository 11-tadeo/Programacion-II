import math
from multimethod import multimethod

class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def producto_punto(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def producto_cruz(self, v):
        rx = self.y * v.z - self.z * v.y
        ry = self.z * v.x - self.x * v.z
        rz = self.x * v.y - self.y * v.x
        return Vector(rx, ry, rz)

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class AlgebraVectorial:
    @multimethod
    def __init__(self):
        self.__a = Vector(0, 0, 0)
        self.__b = Vector(0, 0, 0)

    @multimethod
    def __init__(self, a: Vector, b: Vector):
        self.__a = a
        self.__b = b

    @multimethod
    def perpendicular(self, a: Vector, b: Vector, modo: str):
        modo = modo.lower()
        if modo == "a":
            return (a + b).magnitud() == (a - b).magnitud()
        elif modo == "b":
            return (a - b).magnitud() == (b - a).magnitud()
        elif modo == "c":
            return a.producto_punto(b) == 0.0
        elif modo == "d":
            izq = (a + b).magnitud() ** 2
            der = (a.magnitud() ** 2) + (b.magnitud() ** 2)
            return izq == der

    @multimethod
    def paralela(self, a: Vector, b: Vector, r: float | int):
        return a == (b * r)

    @multimethod
    def paralela(self, a: Vector, b: Vector):
        cruz = a.producto_cruz(b)
        return cruz == Vector(0, 0, 0)

    def proyeccion_de_a_sobre_b(self, a: Vector, b: Vector):
        mag_b = b.magnitud()
        if mag_b == 0:
            print("Error: El vector b no puede ser nulo (0,0,0).")
            return None
        escalar = a.producto_punto(b) / (mag_b**2)
        return b * escalar

    def componente_de_a_en_b(self, a: Vector, b: Vector):
        mag_b = b.magnitud()
        if mag_b == 0:
            print("Error: El vector b no puede ser nulo (0,0,0).")
            return None
        return a.producto_punto(b) / mag_b

if __name__ == "__main__":
    v1 = Vector(3, 0, 0)
    v2 = Vector(0, 4, 0)

    algebra = AlgebraVectorial(v1, v2)

    print("--- VECTORES DE PRUEBA ---")
    print(f"Vector a: {v1}")
    print(f"Vector b: {v2}\n")

    print("--- COMPROBACIONES DE PERPENDICULARIDAD ---")
    print(f"a) |a + b| = |a - b|: {algebra.perpendicular(v1, v2, 'a')}")
    print(f"b) |a - b| = |b - a|: {algebra.perpendicular(v1, v2, 'b')}")
    print(f"c) a . b = 0: {algebra.perpendicular(v1, v2, 'c')}")
    print(
        f"d) |a + b|^2 = |a|^2 + |b|^2: {algebra.perpendicular(v1, v2, 'd')}\n"
    )

    v3 = Vector(1, 2, 3)
    v4 = Vector(2, 4, 6)
    print("--- COMPROBACIONES DE PARALELISMO (Vectores: (1,2,3) y (2,4,6)) ---")
    print(f"e) Con escalar r=0.5 (a = r*b): {algebra.paralela(v3, v4, 0.5)}")
    print(f"f) Con producto cruz a x b = 0: {algebra.paralela(v3, v4)}\n")

    print("--- PROYECCIÓN Y COMPONENTE ---")
    va = Vector(2, 3, 0)
    vb = Vector(4, 0, 0)
    proy = algebra.proyeccion_de_a_sobre_b(va, vb)
    comp = algebra.componente_de_a_en_b(va, vb)
    print(f"g) Proyeccion de {va} sobre {vb}: {proy}")
    print(f"h) Componente de {va} en {vb}: {comp:.2f}")