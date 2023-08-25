"""
Module: geometry_classes

This module defines base and derived geometric classes for calculations and validations.

Classes:
- BaseGeometry: A base class for geometric calculations.

Module Author:
Merit

Last Updated:
24/08/2023

"""
class aMetaClass(type):
    """
    this is a metaclass that is created so that any class that is created inherits the method of this class. hey type is a class that every class created in python inherites from
    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']

class BaseGeometry:
    """
    A base class for geometric calculations.

    """
    def __dir__(cls):
        """
        this is to remove the init subclass
        """
        return [attributes for attributes in super().__dir__() if attributes != '__init_subclass__']
    def area(self):
        """
        Calculate the area of a geometric shape. Not implemented in the base class.

        Raises:
        Exception: Indicates that area calculation is not implemented.
        """
        raise Exception ("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Methods:
    - __init__(width, height): Initialize a Rectangle instance with width and height.
    - area(): Calculate the area of the rectangle.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("must be an integer")
        if width <= 0:
            raise ValueError("must be greater than 0")
        if not isinstance(height, int):
            raise TypeError("must be an integer")
        if height <= 0:
            raise ValueError("must be greater than 0")