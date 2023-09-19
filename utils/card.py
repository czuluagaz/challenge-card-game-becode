class Symbol:
    """
    A class representing a card symbol.

    Attributes:
    - color (str): The color of the symbol, either 'red' or 'black'.
    - icon (str): The icon of the symbol, one of ['♥', '♦', '♣', '♠'].
    """

    def __init__(self, color: str, icon: str):
        """
        Initialize a Symbol object.

        :param color: A string representing the color of the symbol ('red' or 'black').
        :param icon: A string representing the icon of the symbol.
        """
        if color in ["red", "black"]:
            self.color = color
        else:
            raise ValueError("Invalid color. Choose from ['red', 'black']")

        if icon in ['♥', '♦', '♣', '♠']:
            self.icon = icon
        else:
            raise ValueError("Invalid icon. Choose from ['♥', '♦', '♣', '♠']")

    def __str__(self):
        """
        Convert Symbol object to a string representation.
        """
        return f"Symbol: {self.color} {self.icon}"


class Card(Symbol):
    """
    A class representing a playing card.

    Inherits from Symbol and adds the 'value' attribute.

    Attributes:
    - value (str): The value of the card, one of ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'].
    """

    def __init__(self, color: str, icon: str, value: str):
        """
        Initialize a Card object.

        :param color: A string representing the color of the card ('red' or 'black').
        :param icon: A string representing the icon of the card.
        :param value: A string representing the value of the card.
        """
        super().__init__(color, icon)

        if value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.value = value
        else:
            raise ValueError("Invalid card value. Choose from ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']")

    def __str__(self):
        """
        Convert Card object to a string representation.
        """
        return f"Card: {self.color} {self.icon} {self.value}"


'''
1.1 Symbol
In card.py:

Create a class called Symbol with two attributes:

color which is a string.
icon which is a single character out of this list [♥, ♦, ♣, ♠].
1.2 Card
In the same file, create a class Card that inherits from Symbol and add an attribute:

value which is a string (one of ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'])
'''