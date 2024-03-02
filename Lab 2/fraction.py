#
# ================================================================================
# Noah Mattison     9/8/2023
# Lab 1
# Purpose: OOP Intro
# References:
# ================================================================================
class Fraction:
    def __init__(self, numerator, denominator):
        """
        Function: Used to define instance variables
        Params: self, numerator, denominator
        Returns: none
        """
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("TypeError: numerator/denominator values must be integers")
        if denominator == 0:
            raise ValueError("ValueError: Cannot divide by 0, change denominator")
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def __str__(self):
        """
        Function: displays user-friendly string respresentation of a fraction
        Params: self
        Returns: string
        """
        if self.__denominator == 1:
            return str(self.__numerator)
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        """
        Function: Represents a fraction
        Params: self
        Returns: string
        """
        return f"Fraction(numerator={self.__numerator}, denominator={self.__denominator}"

    def getNumerator(self):
        """
        Function: Provides the value of a private numerator
        Params: self
        Returns: Integer
        """
        return self.__numerator

    def getDenominator(self):
        """
        Function: Provides the value of a private denominator
        Params: self
        Returns: Integer
        """
        return self.__denominator

    def setDenominator(self, value):
        """
        Function: Sets a value for the denominator position of a fraction
        Params: self, value
        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError("TypeError: numerator values must be integers")
        if value == 0:
            raise ValueError("ValueError: Cannot divide by 0")
        self.__denominator = value

    def setNumerator(self, value):
        """
        Function: Sets a value for the numerator position of a fraction
        Params: self, value
        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError("TypeError: numerator values must be integers")
        self.__numerator = value
        self.__numerator = value

    def reduce(self):
        """
        Function: Reduces a fraction to its simplest form
        Params: self
        Returns: Integer
        """
        gcd = self.__calcGCD()
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calcGCD(self):
        """
        Function: Calculates the greatest common denominator between two fractions
        Params: self
        Returns: Integer
        """
        a = max(self.__numerator, self.__denominator)
        b = min(self.__numerator, self.__denominator)

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a

# Special mathematical operators

    def __neg__(self):
        """
        Function: Negates a fraction
        Params: self
        Returns: Integer
        """
        return Fraction(-self.__numerator, self.__denominator)

# self is left side, other is right side
    def __add__(self, other):
        """
        Function: Adds two fractions
        Params: self, other
        Returns: Integer
        """
        numerator = self.__numerator * other.getDenominator() + other.getNumerator() * self.__denominator
        denominator = self.__denominator * other.getDenominator()
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """
        Function: Subtracts two fractions
        Params: self, other
        Returns: Integer
        """
        return self.__add__(-other)

    def __mul__(self, other):
        """
        Function: Multiplies two fractions
        Params: self, other
        Returns: Integer
        """
        numerator = self.__numerator * other.getNumerator()
        denominator = self.__denominator * other.getDenominator()
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """
        Function: Divides two fractions
        Params: self, other
        Returns: Integer
        """
        numerator = self.__numerator * other.getDenominator()
        denominator = self.__denominator * other.getNumerator()
        return Fraction(numerator, denominator)

    # Methods for special boolean operators
# ==
    def __eq__(self, other):
        """
        Function: compares 2 fractions using the equality operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction == secondFraction

# !=
    def __ne__(self, other):
        """
        Function: compares 2 fractions using the not equal operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction != secondFraction

# <
    def __lt__(self, other):
        """
        Function: compares 2 fractions using the less than operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction < secondFraction

# <=
    def __le__(self, other):
        """
        Function: compares 2 fractions using the less than or equal operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction <= secondFraction

# >
    def __gt__(self, other):
        """
        Function: compares 2 fractions using the greater than operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction > secondFraction

# >=
    def __ge__(self, other):
        """
        Function: compares 2 fractions using the greater than or less than operator
        Params: self, other
        Returns: Boolean Value
        """
        firstFraction = self.__numerator * other.getDenominator()
        secondFraction = other.getNumerator() * self.__denominator

        return firstFraction >= secondFraction
