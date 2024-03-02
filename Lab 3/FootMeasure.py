#
# ================================================================================
# Noah Mattison     9/28/2023
# Lab 3
# Purpose: Foot Measurement
# References:
# ================================================================================
class FootMeasure:
    def __init__(self, feet=0, inches=0):
        if not(isinstance(feet, int) or isinstance(inches, int)):
            raise TypeError("wrong value")
        if feet < 0 or inches < 0:
            raise ValueError("Values cannot be negative")
        self.__feet = feet
        self.__inches = inches
        self.__adjust()

    def __str__(self):
        """
        Function: displays user-friendly string
        Params: self
        Returns: string
        """
        if self.__inches == 0 and self.__feet != 0:
            return f"{self.__feet} ft. {self.__inches} ins."
        return f"{self.__feet} ft. {self.__inches} ins."

    def getFeet(self):
        """
        Function: Provides the value of a private foot value
        Params: self
        Returns: Integer
        """
        return self.__feet

    def getInches(self):
        """
        Function: Provides the value of a private inch value
        Params: self
        Returns: Integer
        """
        return self.__inches

    def setFeet(self, value):
        """
        Function: Sets a value for the feet
        Params: self, value
        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError("wrong")
        if value < 0:
            raise ValueError("msg")
        self.__feet = value

    def setInches(self, value):
        """
        Function: Sets a value for the inch
        Params: self, value
        Returns: none
        """
        if not isinstance(value, int):
            raise TypeError("wrong")
        if value < 0:
            raise ValueError("wrong")
        self.__inches = value
        if value >= 12:
            self.__adjust()

    def __add__(self, other):
        """
        Function: Adds two values
        Params: self, other
        Returns: Integer
        """
        feet = self.__feet + other.getFeet()
        inches = self.__inches + other.getInches()
        return FootMeasure(feet, inches)

    def __adjust(self):
        """
        Function: changes the value of feet or inches
        Params: self
        returns: none
        """
        self.__feet += self.__inches // 12
        self.__inches = self.__inches % 12

    def __eq__(self, other):
        """
        Function: compares 2 values using the equality operator
        Params: self, other
        Returns: Boolean Value
        """
        measurement1 = self.__feet * 12 + self.__inches
        measurement2 = other.getFeet() * 12 + other.getInches()
        return measurement1 == measurement2

    def __ne__(self, other):
        """
        Function: compares 2 values using the not equal operator
        Params: self, other
        Returns: Boolean Value
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Function: compares 2 values using the less than operator
        Params: self, other
        Returns: Boolean Value
        """
        inches = self.__feet * 12 + self.__inches
        specialInches = other.getFeet() * 12 + other.getInches()
        return inches < specialInches

    def __le__(self, other):
        """
        Function: compares 2 values using the less than or equal operator
        Params: self, other
        Returns: Boolean Value
        """
        inches = self.__feet * 12 + self.__inches
        specialInches = other.getFeet() * 12 + other.getInches()
        return inches <= specialInches
    
    def __gt__(self, other):
        """
        Function: compares 2 values using the greater than operator
        Params: self, other
        Returns: Boolean Value
        """
        inches = self.__feet * 12 + self.__inches
        specialInches = other.getFeet() * 12 + other.getInches()
        return inches > specialInches

    def __ge__(self, other):
        """
        Function: compares 2 values using the greater than or less than operator
        Params: self, other
        Returns: Boolean Value
        """
        inches = self.__feet * 12 + self.__inches
        specialInches = other.getFeet() * 12 + other.getInches()
        return inches >= specialInches
