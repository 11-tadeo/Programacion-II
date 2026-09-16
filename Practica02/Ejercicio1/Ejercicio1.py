import math
from multimethod import multimethod

class MiPunto:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    @multimethod
    def distancia(self, otro_punto: "MiPunto"):
        dx = self.__x - otro_punto.get_x()
        dy = self.__y - otro_punto.get_y()
        return math.sqrt(dx**2 + dy**2)

    @multimethod
    def distancia(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return math.sqrt(dx**2 + dy**2)

p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print(f"Punto 1: ({p1.get_x()}, {p1.get_y()})")
print(f"Punto 2: ({p2.get_x()}, {p2.get_y()})")

print(f"Distancia (pasando objeto): {p1.distancia(p2)}")

print(f"Distancia (pasando x e y): {p1.distancia(10, 30.5)}")