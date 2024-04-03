from io import UnsupportedOperation
from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return self + -other
    def __neg__(self,):
        return Vector(-self.x, -self.y)
    def __mul__(self, k):
        return Vector(k * self.x, k * self.y)
    def __rmul__(self, k):
        return self.__mul__(k)
    def __floordiv__(self, k):
        return Vector(self.x // k, self.y // k)
    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)
    
    def dot(self, other):
        return self.x * other.x + self.y + other.y
    def cross(self, other): raise UnsupportedOperation
    def norm(self):
        return sqrt(self.dot(self))
    def magnitude(self):
        return self.norm()
    def unit_vector(self):
        return self / self.magnitude()
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __isub__(self, other):
        self.x += -other
        return self

    def __imul__(self, k):
        self.x *= k
        self.y *= k
        return self
    

if __name__ == "__main__":
    print("Wrong folder this is Vector.py!")
    print("Run game.py to play the game!")