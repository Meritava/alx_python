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


class BaseGeometry:
    """
    A base class for geometric calculations.

    """
    def __dir__(cls):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list