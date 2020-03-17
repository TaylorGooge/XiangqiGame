class Error(Exception):
    """
    Base Class for other Exceptions
    """
    pass


class InvalidMoveError(Error):
    """
    This error is raised when the player tries to pass a invalid move, for example "53" or "2A".
    """
    pass


class Piece:
    """
    This is the base class for all pieces in the game. All data members and attributes are
    inherited by the other piece- type classes.
    """

    def __init__(self, color, location):
        """
        Instantiates a piece object with color, location, and potential_moves attributes.
        :param color: Red or Black
        """
        self._color = color.lower()
        self._potential_moves = None
        self._location = location

    def __repr__(self):
        if self._color == "red":
            return f'\033[0;31m{self._title}\033[0m"'
        else:
            return f"{self._title}"

    def get_location(self):
        """
        The function returns the location of the piece object.
        """
        return self._location

    def update_location(self, value):
        """
        This function updates the piece object's location.
        :param value: Location of the piece object.
        :return:
        """
        self._location = value

    def get_color(self):
        """
        This is a getter method for the color of the piece object.
        :return: color of the Piece object.
        """
        return self._color

    def col_to_num(self, column):
        """
        Helper for functions which require numerical manipulation of columns. Converts the alpha value into a
        numerical value.
        :param column: The column value to be converted to a numerical value
        :return: A numerical representation of column key
        """
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        char_to_int_index = 0

        for char in letters:
            if char != column:
                char_to_int_index += 1
            else:
                char_to_int_index += 1
                return char_to_int_index

    def num_to_col(self, column):
        """
        Helper or functions in which column values where converted to numerical values for comparison. This function
        converts to column value back into an alpha so that it can be understood by the XiangqiGame class.
        :param column: A numerical column value to be converted to an alpha value.
        :return: An alpha representation of a column key
        """
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        index = 1

        for char in letters:
            if index == column:
                index += 1
                return char
            else:
                index += 1

    def move_capture_check(self, temp_start_obj, temp_end_obj):
        """
        This function validates that the end move is either an empty space or is occupied by the opponent player's
        piece.
        :param temp_start_obj: The piece occupying the starting space.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :return: True/ False
        """

        if temp_end_obj is None:
            return True
        elif temp_end_obj.get_color() != temp_start_obj.get_color():
            return True
        else:
            return False

    def castle_check(self, end):
        """
        This function is used by the General and Advisor classes to ensure the piece does not move outside the "castle".
        :param end: The ending location of the piece.
        :return: True/ False
        """
        end_col = int(self.col_to_num(end[0]))
        if self.get_color() == 'red':
            if 4 <= end_col <= 6:
                if 1 <= int(end[1:]) <= 3:
                    return True
        elif self.get_color() == "black":
            if 4 <= end_col <= 6:
                if 8 <= int(end[1:]) <= 10:
                    return True

    def get_potential_moves(self):
        """
        This function returns a set of the valid moves the player could make during their next turn.
        :return: set of valid moves
        """
        return self._potential_moves

    def update_potential_moves(self, update):
        """
        At the conclusion of a valid move the potential_moves variable is updated with all valid moves the player could
        make during their next turn.
        :param update: set of valid moves
        :return: None
        """
        self._potential_moves = set(update)