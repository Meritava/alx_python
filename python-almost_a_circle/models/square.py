# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle with equal width and height.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.

        Args:
            size (int): Size of the square (both width and height).
            x (int, optional): X-coordinate of the position. Defaults to 0.
            y (int, optional): Y-coordinate of the position. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)  # Call the Rectangle class constructor
        # Since a square has equal width and height, we pass 'size' for both width and height.

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: String in the format '[Square] (<id>) <x>/<y> - <size>'.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
