"""
This module contains functions for class and object checks.
"""
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
    obj: The object to be checked for class membership.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object is an instance of the specified class, False otherwise.
    """
    return isinstance(obj, a_class)