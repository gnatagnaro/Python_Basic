# заметил, что уменьшилось количество заданий в домашней работе, поэтому эту задачу можно было не делать

import math


class Circle:

    def __init__(self, x=0, y=0, R=1):
        self.x = x
        self.y = y
        self.R = R

    def find_square(self):
        self.S = math.pi * (self.R ** 2)
        return self.S

    def find_perimetr(self):
        self.P = 2 * math.pi * self.R
        return self.P

    def increase(self, k):
        self.R = self.R * k
        return self.R

    def intersects(self, other):
        # self.AB = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        # if abs(self.R - other.R) <= abs(self.AB) <= abs(self.R + other.R):
        #     return 'Окружности пересекаются'
        # return 'Окружности не пересекаются'
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.R + other.R) ** 2


x = Circle()
y = Circle()
print(x.intersects(y))
print(x.find_square())
print(x.find_perimetr())
print(x.increase(10))
