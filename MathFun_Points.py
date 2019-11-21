class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + " ,  "+str(self.y)+"]"

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def __mul__(self, other):
        if type(other) is Point2D:
            self.x = self.x * other.x
            self.y = self.y * other.y
            return self
        elif type(other) is str:
            self.x = self.x * float(other)
            self.y = self.y * float(other)
            return self
        else:
            self.x = self.x * other
            self.y = self.y * other
            return self



    def __truediv__(self, other):
        self.x = self.x / other.x
        self.y = self.y / other.y
        return self

    def cross_product(self, other):
        return (self.x * other.y)-(self.y * other.x)


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[" + str(self.x) + " ,  "+str(self.y)+ " ,  " + str(self.z)+ "]"


if __name__ == '__main__':
    a = Point2D(1,2)
    b = Point3D(1,2,3)
    print(b)