from baseclasses import Piece


class Chariot(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and potential moves data members.
        :param color: Red or Black
        :param location: The space the piece occupies on the board, if any.
        """
        self._title = "C"
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

    def chariot_move_check(self, end, board_object, temp_end_obj):
        """
        This function validates the proposed move.
        :param board_object: The board class object.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The space to move the Chariot to
        :return: True or False
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
        At the conclusion of a valid move the piece's possible moves are updated with the current attacked spaces.
        :param board_object: The board class object.
        :param end: The space the piece moved to at the conclusion of a valid move.
        :return: None
        """
        potential_moves = []

        # end is new start
        start = end

        # horizontal leftward move
        counter = self.col_to_num(start[0]) - 1

        end = 1
        skipped_space = False
        while counter >= end:
            temp = self.num_to_col(counter)
            temp = temp + start[1:]
            temp_obj = board_object.get_space_info(temp)
            if temp_obj is not None and skipped_space is False:
                if temp_obj.get_color() == self.get_color():
                    break
                else:
                    potential_moves.append(temp)
                    break
            elif temp_obj is None and skipped_space is False:
                potential_moves.append(temp)
                counter -= 1

        # horizontal rightward move
        counter = self.col_to_num(start[0]) + 1
        end = 9
        skipped_space = False
        if counter <= end:
            while counter <= end:
                temp = self.num_to_col(counter) + start[1:]
                temp_obj = board_object.get_space_info(temp)
                if temp_obj is not None and skipped_space is False:
                    if temp_obj.get_color() == self.get_color():
                        break
                    else:
                        potential_moves.append(temp)
                        break
                elif temp_obj is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter += 1

        # upward vertical move
        counter = int(start[1:]) + 1
        end = 10
        skipped_space = False
        if counter > 0:
            while counter <= end:
                temp = start[0] + str(counter)
                temp_obj = board_object.get_space_info(temp)
                if temp_obj is not None and skipped_space is False:
                    if temp_obj.get_color() == self.get_color():
                        break
                    else:
                        potential_moves.append(temp)
                        break
                elif temp_obj is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter += 1

            # downward vertical
        counter = int(start[1:]) - 1
        end = 1
        skipped_space = False
        if counter > 0:
            while counter >= end:
                temp = start[0] + str(counter)
                temp_obj = board_object.get_space_info(temp)
                if temp_obj is not None and skipped_space is False:
                    if temp_obj.get_color() == self.get_color():
                        break
                    else:
                        potential_moves.append(temp)
                        break
                elif temp_obj is None and skipped_space is False:
                    potential_moves.append(temp)
                    counter -= 1

        self.update_potential_moves(potential_moves)
