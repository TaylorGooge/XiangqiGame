from baseclasses import Piece


class General(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and potential moves data members.
        :param color: Red or Black
        :param location: The space the piece current occupies, if any.
        """
        self._title = "G"
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

    def general_move_check(self, start, end, board_object, temp_end_obj):
        """
        This function validates the proposed move.
        :param start: The start position of the move.
        :param end: The end position of the move.
        :param board_object: The board class object.
        :param temp_end_obj: The object to be captured on the end space, if any.
        :return: True / False
        """

        if self.castle_check(end) is True:
            if self.move_capture_check(self, temp_end_obj) is True:
                pass
        else:
            return False

        self.possible_moves(board_object, self.get_location())
        if end in self.get_potential_moves():
            if self.general_invalid_check_moves(start, end, board_object) is True:
                board_object.update_pieces_list(end)
                return True

    def general_invalid_check_moves(self, start, end, board_object):
        """
        This function determines whether the proposed move would leave the general in check.
         :param start: The start position of the move.
        :param end: The end position of the move.
        :param board_object: The board class object.
        :return: False or None
        """
        potential_moves = []
        potential_moves.append(start)

        start = end

        # check for flying general
        if self.get_color() == "red":
            general_covered = False
            base = 10
            counter = int(start[1:]) + 1
            while counter <= base:
                temp = start[0] + str(counter)
                if board_object.get_space_info(temp) is None:
                    counter += 1
                elif board_object.get_space_info(temp) is not None and general_covered is False:
                    result = board_object.get_space_info(temp)
                    counter += 1
                    if result.get_title() == "G" and result.get_color() != self.get_color():
                        return False
                    else:
                        general_covered = True
                        counter += 1
                else:
                    counter += 1

        elif self.get_color() == "black":
            general_covered = False
            base = 1
            counter = int(start[1:]) - 1
            while counter >= base:
                temp = start[0] + str(counter)
                if board_object.get_space_info(temp) is None:
                    counter -= 1
                elif board_object.get_space_info(temp) is not None and general_covered is False:
                    result = board_object.get_space_info(temp)
                    counter -= 1
                    if result.get_title() == "G" and result.get_color() != self.get_color():
                        counter -= 1
                        return False
                    else:
                        general_covered = True
                        counter -= 1
                else:
                    counter -= 1

        # check to see if move would put general in check with other pieces
        if self.get_color() == "red":
            for piece in board_object.get_black_pieces():
                if piece.get_potential_moves() is not None:
                    for moves in piece.get_potential_moves():
                        if moves == end:
                            return False
                        else:
                            return True
        elif self.get_color() == "black":
            for piece in board_object.get_red_pieces():
                if piece.get_potential_moves() is not None:
                    for moves in piece.get_potential_moves():
                        if moves == end:
                            return False
                        else:
                            return True

    def possible_moves(self, board_object, end):
        """
        At the conclusion of a valid move the piece's possible moves are updated with the current attacked spaces.
        :param board_object: The board class object.
        :param end: The space the piece moved to at the conclusion of a valid move.
        :return: None
        """
        allowable_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        potential_moves = []
        start = end

        for moves in allowable_moves:
            if 4 <= self.col_to_num(start[0]) + moves[0] <= 6:
                if self.get_color() == "red" and 1 <= int(start[1:]) + moves[
                    1] <= 3 or self.get_color() == "black" and 7 <= int(start[1:]) + moves[1] <= 10:
                    temp = self.num_to_col(self.col_to_num(start[0]) + moves[0]) + str(int(start[1:]) + moves[1])
                    temp_obj = board_object.get_space_info(temp)
                    if temp_obj is None or temp_obj.get_color() != self.get_color():
                        potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
