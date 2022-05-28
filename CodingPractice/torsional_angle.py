'''
Problem: You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. You are required to print the angle between 
    the plane made by the points A, B, C and B, C, D in degrees(not radians). Let the angle be PHI.
    cos(PHI) = (X.Y)/|X||Y| where
    X.Y (dot product)
    X = AB x BC (Cross Product) and AB = B - A
    Y = BC x CD

    Input Format: One line of input containing the space separated floating number values of the and coordinates of a point.

    Output Format: Output the angle correct up to two decimal places.
'''
import math

class Points(object):
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __sub__(self, vecB):
        return Points((vecB.i - self.i), (vecB.j - self.j), (vecB.k - self.k))

    def dot(self, vecB):
        return ((self.i * vecB.i) + (self.j * vecB.j) + (self.k * vecB.k))

    def cross(self, vecB):
        return Points(((self.j * vecB.k) - (self.k * vecB.j)),((self.k * vecB.i) - (self.i * vecB.k)), ((self.i * vecB.j) - (self.j * vecB.i)))
    
    def absolute(self):
        return pow((self.i ** 2 + self.j ** 2 + self.k ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
