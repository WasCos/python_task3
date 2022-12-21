from NOD_2 import *

class RationalNumber:

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError('Знаменатель не может равняется нулю')
        self.num = abs(num)
        self.den = abs(den)
        self.sign = self.__sign(num, den)

    @property
    def positive(self):
        return self.sign >= 0

    def float_1(self):
        return self.sign * self.num / self.den

    float = property(float_1)

    def __repr__(self):
        return f'{self.sign * self.num}/{self.den}'

    def __str__(self):
        return str(self.float)

    @staticmethod
    def __sign(num, den):
        if num < 0 and den < 0:
            return 1
        if num < 0 or den < 0:
            return -1
        else:
            return 1

    def __add__(self, other):
        new_num = self.sign * self.num * other.den + self.den * other.sign * other.num
        new_den = self.den * other.den
        both_gcd = get_gcd(new_num, new_den)
        return RationalNumber(new_num//both_gcd,new_den//both_gcd)

    def __sub__(self, other):
        new_num = self.sign * self.num * other.den - self.den * other.sign * other.num
        new_den = self.den * other.den
        both_gcd = get_gcd(new_num, new_den)
        return RationalNumber(new_num//both_gcd,new_den//both_gcd)

    def __mul__(self, other):
        new_num = self.num * other.num * self.sign * other.sign
        new_den = self.den * other.den
        both_gcd = get_gcd(new_num, new_den)
        return RationalNumber(new_num//both_gcd,new_den//both_gcd)

    def __truediv__(self, other):
        new_num = self.num * other.den * self.sign * other.sign
        new_den = self.den * other.num 
        return RationalNumber(new_num,new_den)



# # Пунк 1
# rnum_1 = RationalNumber(num=2, den=5)
# print('rnum_1:', rnum_1.num, rnum_1.den, rnum_1.positive)
# rnum_2 = RationalNumber(num=-3, den=7)
# print('rnum_2:', rnum_2.num, rnum_2.den, rnum_2.positive)
# # Пунк 2
# rnum_1 = RationalNumber(num=2, den=5)
# print('rnum_1:', rnum_1.float)
# rnum_2 = RationalNumber(num=-3, den=7)
# print('rnum_2:', rnum_2.float)
# # Пунк 3
# rnum_1 = RationalNumber(num=2, den=5)
# print('rnum_1:', repr(rnum_1), str(rnum_1))
# rnum_2 = RationalNumber(num=-3, den=7)
# print('rnum_2:', repr(rnum_2), str(rnum_2))
# # Пунк 4
# rnum_1 = RationalNumber(num=2, den=5)
# rnum_2 = RationalNumber(num=-3, den=7)
# print(repr(rnum_1 + rnum_2), repr(rnum_1 - rnum_2), repr(rnum_1 * rnum_2), repr(rnum_1 / rnum_2))