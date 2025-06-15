# Задание 1 =================================================
from functools import total_ordering


class Soda:
    def __init__(self, additive: str = None):
        self.additive = additive

    def show_my_drink(self):
        return f"Газировка и {self.additive}" if self.additive else f"Обычная газировка"

soda_1 = Soda()
soda_2 = Soda("Ваниль")
print(soda_1.show_my_drink())
print(soda_2.show_my_drink())

# Задание 2 =================================================
class TriangleChecker:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float))):
            return f"Нужно вводить только числа!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return f"С отрицательными числами ничего не выйдет!"
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return f"Ура, можно построить треугольник!"
        else:
            return f"Жаль, но из этого треугольник не сделать."

tr = TriangleChecker(9, 5, 7)
print(tr.is_triangle())

# Задание 3 =================================================
class KgToPounds:
    def __init__(self, __kg: int | float):
        self.__kg = __kg
        if not isinstance(self.__kg, (int, float)):
            raise ValueError

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        self.__kg = value

    def to_pounds(self):
        return self.__kg*2.205

    # def get_kg(self):
    #     return self.__kg
    #
    # def set_kg(self, value):
    #     self.__kg = value


weight = KgToPounds(10)
print(weight.kg)
weight.kg=12
print(weight.kg)
print(weight.to_pounds())

# Задание 4 =================================================
@total_ordering
class RealString:
    def __init__(self, string: str):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)

rs1 = RealString('Apple')
rs2 = RealString('Яблоко')
print(rs2 > rs1)
print('Яблоко' == rs2)

# Задание 5 =================================================
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height

re1 = Rectangle(5, 8)
print(re1)
print(re1.get_area())
print(re1.get_perimeter())
print(re1.is_square)

# Задание 6 =================================================
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        return self.name

    @property
    def set_name(self):
        def setter(new_name):
            self.name = new_name
        return setter

    @staticmethod
    def is_adult(self):
        return self.age >= 18

    @classmethod
    def create_from_string(cls, s: str):
        s = s.split("-")
        name = s[0]
        age = int(s[1])
        gender = s[2]
        return cls(name, age, gender)

p1 = Person("Алексей", 28, "М")
print(p1)
print(p1.get_name())
p1.set_name("Alexey")
print(p1)
print(Person.is_adult(p1))
p2 = Person.create_from_string("Alexey-27-M")
print(p2)
