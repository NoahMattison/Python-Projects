#
# ================================================================================
# Noah Mattison     9/8/2023
# Lab 1
# Purpose: OOP Intro
# References:
# ================================================================================

from fraction import Fraction


def main():
    print("creating fractions: (1, 2), (-1, 4), (0, 2), (4, 1), and (2, 4)")
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-1, 4)
    frac3 = Fraction(0, 2)
    frac4 = Fraction(4, 1)
    frac5 = Fraction(2, 4)

    print("\n__str__ method: ")
    print(f"Fraction 1 should be 1/2:\n Value: {frac1}")
    print(f"Fraction 5 should display the reduce method and be 1/2: \n Value: {frac5}")

    print("\n__add__: ")
    print(f"{frac1} + {frac2} should be 1/4:\n Value: {frac1+frac2}")

    print("\n__sub__: ")
    print(f"{frac2} - {frac3} should be -1/4:\n Value: {frac2-frac3}")

    print("\n__mul__: ")
    print(f"{frac1} * {frac4} should be 2:\n Value: {frac1*frac4}")

    print("\n__truediv__: ")
    print(f"{frac1} / {frac2} should be -2:\n Value: {frac1/frac2}")

    print("\n__eq__: ")
    print(f"{frac1} == {frac5} should be equal:\n Value: {frac1 == frac5}")

    print("\n__ne__: ")
    print(f"{frac1} != {frac3} should be True:\n Value: {frac1 != frac3}")

    print("\n__lt__: ")
    print(f"{frac3} < {frac1} should be True:\n Value: {frac3 < frac1}")

    print("\n__le__: ")
    print(f"{frac1} <= {frac5} should be True:\n Value: {frac1 <= frac5}")
    print(f"{frac4} <= {frac1} should be False:\n Value: {frac4 <= frac1}")

    print("\n__gt__: ")
    print(f"{frac4} > {frac5} should be True:\n Value: {frac4 > frac1}")

    print("\n__ge__: ")
    print(f"{frac4} >= {frac3} should be True:\n Value: {frac4 >= frac3}")
    print(f"{frac3} >= {frac1} should be False:\n Value: {frac3 >= frac1}")


if __name__ == '__main__':
    main()
