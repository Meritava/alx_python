# models/rectangle.py
from models.base import Base  # Import the Base class from the base module

class Rectangle(Base):
    """
    Represents a rectangle with width, height, position (x, y), and an ID.
    Inherits from the Base class for ID management.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance.
        
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the position. Defaults to 0.
            y (int, optional): Y-coordinate of the position. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        """
        super().__init__(id)  # Call the Base class constructor with id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        """Getter method for the width."""
        return self.__width

    @get_width.setter
    def get_width(self, value):
        """Setter method for the width."""
        
        self.__width = value

    @property
    def get_height(self):
        """Getter method for the height."""
        return self.__height

    @get_height.setter
    def get_height(self, value):
        """Setter method for the height."""
        
        self.__height = value

    @property
    def get_x(self):
        """Getter method for the x-coordinate."""
        return self.__x

    @get_x.setter
    def x(self, value):
        """Setter method for the x-coordinate."""
        
        self.__x = value

    @property
    def get_y(self):
        """Getter method for the y-coordinate."""
        return self.__y

    @get_y.setter
    def get_y(self, value):
        """Setter method for the y-coordinate."""
       
        self.__y = value