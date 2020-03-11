from baseclasses import Piece

class Cannon(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and potential moves data members.
        :param color: Red or Black
        :param location: The current space the piece occupies.
        """
        self._title = "Can"
        super().__init__(color, location)

    def get_title(self):
        """
        This is a getter function that returns the title of the General object.
        :return: title of the general object.
        """
        return self._title

    def cannon_move_check(self, end, board_object, temp_end_obj):
        """
        This function validates a proposed cannon move.
        :param board_object: The board class object.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The location the cannon moves to
        :return: True/ False
        """
        if self.move_capture_check(self, temp_end_obj) is True:
            pass
        else:
            return False
        self.possible_moves(board_object, self.get_location())
        if end in self.get_potential_moves():
            board_object.update_pieces_list(end)
            return True

    def possible_moves(self, board_object, end):
        """
        At the conclusion of a valid move the pieces current attacked squares are updated.
        :param board_object: The board class object.
        :param end: The space the piece moved to at the conclusion of the last turn
        :return: None
        """

        potential_moves = []
        start = end

        # vertical upward move
        counter = int(start[1:]) - 1
        base = 1
        if counter >= 1:
            skipped_space = False
            while counter >= base:
                temp = start[0] + str(counter)
                result = board_object.get_space_info(temp)
                if result is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter -= 1
                elif result is not None and skipped_space is False:
                    skipped_space = True
                    counter -= 1
                elif result is not None and skipped_space is True and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                    counter -= 1
                else:
                    counter -= 1

        # vertical downward move
        counter = int(start[1:]) + 1
        base = 10
        if counter <= base:
            skipped_space = False
            while counter <= base:
                temp = start[0] + str(counter)
                result = board_object.get_space_info(temp)
                if result is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter += 1
                elif result is not None and skipped_space is False:
                    skipped_space = True
                    counter += 1
                elif result is not None and skipped_space is True and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                    counter += 1
                else:
                    counter += 1

        # horizontal rightward move
        counter = self.col_to_num(start[0]) + 1
        base = 9
        if counter <= base:
            skipped_space = False
            while counter <= 9:
                temp = self.num_to_col(counter) + start[1:]
                result = board_object.get_space_info(temp)
                if result is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter += 1
                elif result is not None and skipped_space is False:
                    skipped_space = True
                    counter += 1
                elif result is not None and skipped_space is True and result.get_color() != self.get_color():
                    skipped_space = None
                    potential_moves.append(temp)
                    counter += 1
                else:
                    counter += 1

        # horizontal leftward move
        counter = self.col_to_num(start[0]) - 1
        base = 1
        if counter >= base:
            skipped_space = False
            while counter >= base:
                temp = self.num_to_col(counter) + start[1:]
                result = board_object.get_space_info(temp)
                if result is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter -= 1
                elif result is not None and skipped_space is False:
                    skipped_space = True
                    counter -= 1
                elif result is not None and skipped_space is True and result.get_color() != self.get_color():
                    skipped_space -= 1
                    potential_moves.append(temp)
                    counter -= 1
                else:
                    counter -= 1

        self.update_potential_moves(potential_moves)
