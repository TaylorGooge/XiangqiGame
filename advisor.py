from baseclasses import Piece


class Advisor(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and potential moves data members.
        :param color: Red or Black
        :param location: The space the piece occupies on the board, if any.
        """
        self._title = "A"
        super().__init__(color, location)

    def __repr__(self):
        if self._color == "red":
            return f'{"R"}{self._title}'
        else:
            return f'{"B"}{self._title}'

    def get_title(self):
        """
        This is a getter function that returns the title of the General object.
        :return: title of the general object.
        """
        return self._title

    def advisor_move_check(self, end, temp_end_obj, board_object):
        """
        This function contains all of the logic to determine a valid Advisor move.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The space to move the Advisor to
        :return: True or False
        """

        if self.move_capture_check(self, temp_end_obj) is True:
            if self.castle_check(end) is True:
                pass
        else:
            return False

        self.possible_moves(board_object, self.get_location())
        if end in self.get_potential_moves():
            board_object.update_pieces_list(end)
            return True

    def possible_moves(self, board_object, end):
        """
        At the conclusion of a valid move the pieces attacked spaces are updated.
        :param end: The location the pieced moved to at the conclusion of the last turn.
        :param board_object: The board class object.
        :return: None
        """
        allowable_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        potential_moves = []
        start = end

        for moves in allowable_moves:
            if 1 <= self.col_to_num(start[0]) + moves[0] <= 9 and 1 <= int(start[1:]) + moves[1] <= 10:
                temp = self.num_to_col(self.col_to_num(start[0]) + moves[0]) + str(int(start[1:]) + moves[1])
                temp_obj = board_object.get_space_info(temp)
                if self.castle_check(temp) is True:
                    if temp_obj is None or temp_obj.get_color() != self.get_color():
                        potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
