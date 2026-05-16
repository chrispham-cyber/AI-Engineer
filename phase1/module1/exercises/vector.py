class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

print(v1)
print(v2)
print("=" * 30)

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 5 = {v1 * 5}")
print(f"v1 · v2 = {v1.dot(v2)}")
print(f"|v1| = {v1.magnitude():.03f}")
print(f"|v2| = {v2.magnitude():.03f}")