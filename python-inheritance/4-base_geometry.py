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