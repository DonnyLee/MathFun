class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + " ,  "+str(self.y)+"]"


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