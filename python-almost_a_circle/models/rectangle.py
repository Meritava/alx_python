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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """
        self.validate_positive_integer(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """
        self.validate_positive_integer(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        self.validate_non_negative_integer(value, 'x')
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.
        """
        self.validate_non_negative_integer(value, 'y')
        self.__y = value

    def validate_positive_integer(self, value, attribute_name):
        """
        Validates that the given value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, value, attribute_name):
        """
        Validates that the given value is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
    def area(self):
        """
        Calculates and returns the area value of the Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height
    def display(self):
        """
        Displays the Rectangle instance by printing it with '#' characters.
        """
        #for _ in range(self.height):
            #print('#' * self.width)
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Overrides the __str__ method to provide a custom string representation.

        Returns:
            str: A formatted string representation of the Rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
    def update(self, *args):
        """
        Update the attributes of the Rectangle instance based on provided arguments.

        Args:
            *args: Variable-length arguments.
                1st argument (int): ID attribute.
                2nd argument (int): Width attribute.
                3rd argument (int): Height attribute.
                4th argument (int): X attribute.
                5th argument (int): Y attribute.
        """
        num_args = len(args)  #This line calculates the number of arguments passed to the update method by counting the elements in the args tuple
        if num_args >= 1:  #This conditional statement checks if at least one argument was provided. If so, it assigns the first argument to the id attribute of the rectangle.
            self.id = args[0]
        if num_args >= 2:    #This conditional statement checks if at least two arguments were provided. If so, it assigns the second argument to the width attribute of the rectangle.
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]