#
# ================================================================================
# Noah Mattison     9/28/2023
# Lab 3
# Purpose: Foot Measurement
# References:
# ================================================================================

from FootMeasure import FootMeasure


def main():
    print("Foot Measurements: none, 5 ft., 5 ft. 8 in., 68 in.")
    measure1 = FootMeasure()
    measure2 = FootMeasure(feet=5)
    measure3 = FootMeasure(feet=5, inches=8)
    measure4 = FootMeasure(inches=68)

    print("\n__str__ method: ")
    print(f"Measure3 should look like 5 ft. 8 in. : {measure3}")
    print(f"Measure1 should look like 0 ft. 0 in. : {measure1}")

    print("\n__add__: ")
    print(f"{measure2} + {measure3} should be 10 ft. 8 in. : {measure2+measure3}")

    print("\n__eq__: ")
    print(f"{measure4} == {measure3} should be True:\n Value: {measure4 == measure3}")

    print("\n__ne__: ")
    print(f"{measure1} != {measure4} should be True:\n Value: {measure1 != measure4}")

    print("\n__lt__: ")
    print(f"{measure2} < {measure3} should be True:\n Value: {measure2 < measure3}")

    print("\n__le__: ")
    print(f"{measure3} <= {measure4} should be True:\n Value: {measure3 <= measure4}")
    print(f"{measure3} <= {measure2} should be False:\n Value: {measure3 <= measure2}")

    print("\n__gt__: ")
    print(f"{measure4} > {measure2} should be True:\n Value: {measure4 > measure2}")

    print("\n__ge__: ")
    print(f"{measure4} >= {measure2} should be True:\n Value: {measure4 >= measure2}")
    print(f"{measure2} >= {measure4} should be False:\n Value: {measure2 >= measure4}")


if __name__ == '__main__':
    main()
    