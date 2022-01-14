import pytest
from fraction import Fraction


class TestFraction:
    def setup(self):
        self.f1 = Fraction(3, 5)
        self.f2 = Fraction(4, 5)
        self.f3 = Fraction(7, 5)

    def test_str(self):
        assert str(self.f1) == "3/5"

    def test_add(self):
        assert str(self.f1 + self.f2) == str(self.f3)

    def test_sub(self):
        assert str(self.f2 - self.f1) == "1/5"

    def test_mult(self):
        assert str(self.f1 * self.f2) == "12/25"

    def test_ne(self):
        assert str(self.f1) != str(self.f2)
