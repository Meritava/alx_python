"""
Module: rectangle.py
This module defines the Rectangle class, which inherits from the Base class.
"""
from models.base import Base

class Rectangle(Base):
     """
    Represents a rectangle, a subclass of the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """
     def __init__(self, width, height, x=0, y=0, id=None):
          """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier of the rectangle.
        """
          super().__init__(id)
          self.__width = width
          self.__height = height
          self.__x = x
          self.__y = y

          @property
          def width(self):
               """
               getter for the width
               """
               return self.__width
          @width.setter
          def width(self, value):
               """
               setter for width
               """
               self.__width = value