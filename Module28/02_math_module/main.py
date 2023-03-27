from math import pi


class MyMath:
    """
    Класс, состоящий из 4-х математических методов:
        вычисление длины окружности,
        вычисление площади окружности,
        вычисление объёма куба,
        вычисление площади поверхности сферы.
    """
    @classmethod
    def circle_len(cls, radius: (int, float)) -> (int, float):
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: (int, float)) -> (int, float):
        return pi * (radius ** 2)

    @classmethod
    def cube_vol(cls, side: (int, float)) -> (int, float):
        return side ** 3

    @classmethod
    def sphere_surf_sq(cls, radius: (int, float)) -> (int, float):
        return 4 * pi * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(side=7)
res_4 = MyMath.sphere_surf_sq(radius=8)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
