from __future__ import annotations

# gcd function
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Fraction Class
class Fraction:
    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.num = numerator // g
        self.den = denominator // g

    def __str__(self) -> str:
        return str(f"{self.num}/{self.den}")

    def show(self) -> None:
        print(str(self))

    def __add__(self, other) -> Fraction:
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other) -> Fraction:
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other) -> bool:
        return (self.num * other.den) == (self.den * other.num)

    def __lt__(self, other) -> bool:
        return (self.num * other.den) < (self.den * other.num)

    def __gt__(self, other) -> bool:
        return (self.num * other.den) > (self.den * other.num)

    def __mul__(self, other) -> Fraction:
        new_num = self.num * other.num
        new_den = self.den * other.den
        g = gcd(new_num, new_den)
        return Fraction(new_num // g, new_den // g)

    def __truediv__(self, other) -> Fraction:
        return self * Fraction(other.den, other.num)


# Test
Fraction(3, 5).show()
(Fraction(3, 5) + Fraction(4, 5)).show()
(Fraction(4, 5) - Fraction(3, 2)).show()
(Fraction(4, 5) * Fraction(3, 2)).show()
(Fraction(4, 5) / Fraction(3, 2)).show()
(Fraction(4, 5) == Fraction(3, 2))
print(Fraction(4, 5) < Fraction(3, 2))
print(Fraction(4, 5) > Fraction(3, 2))
