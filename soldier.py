from baseclasses import Piece



class Soldier(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and potential moves data members.
        :param color: Red or Black.
        :param location: The space the piece currently occupies.
        """
        self._title = "S"
        super().__init__(color, location)

    def get_title(self):
        """
        This is a getter function that returns the title of the General object.
        :return: title of the general object.
        """
        return self._title

    def soldier_move_check(self, end, temp_end_obj, board_object):
        """
        This function validates a proposed solider move.
        :param board_object: The board class object.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The space to move the Soldier to
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
        At the conclusion of a valid move the pieces currently attacked squares are updated.
        :param end: The location the soldier object moved to
        :param board_object: The board class object.
        :return: None
        """

        potential_moves = []
        start = end

        if self.get_color() == "red":
            if int(start[1:]) <= 5:
                temp = start[0] + str(int(start[1:]) + 1)
                result = board_object.get_space_info(temp)
                if result is not None and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                elif result is None:
                    potential_moves.append(temp)
            # if across the river try side to side
            elif int(start[1:]) >= 6:
                temp = self.col_to_num(start[0]) - 1
                if temp >= 1:
                    temp = self.num_to_col(temp) + start[1:]
                    result = board_object.get_space_info(temp)
                    if result is not None and result.get_color() != self.get_color():
                        potential_moves.append(temp)
                    elif result is None:
                        potential_moves.append(temp)
                if self.col_to_num(start[0]) + 1 <= 9:
                    temp = self.num_to_col(self.col_to_num(start[0]) + 1) + str(start[1:])
                    result = board_object.get_space_info(temp)
                    if result is not None and result.get_color() != self.get_color():
                        potential_moves.append(temp)
                    elif result is None:
                        potential_moves.append(temp)
                temp = start[0] + str(int(start[1:]) + 1)
                result = board_object.get_space_info(temp)
                if result is not None and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                elif result is None:
                    potential_moves.append(temp)

        if self.get_color() == "black":
            if int(start[1:]) >= 6 and int(start[1:]) - 1 >= 1:
                temp = start[0] + str(int(start[1]) - 1)
                result = board_object.get_space_info(temp)
                if result is not None and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                elif result is None:
                    potential_moves.append(temp)
                # if the river is crossed check side to side
            elif int(start[1:]) <= 5 and self.col_to_num(start[0]) - 1 >= 1:
                temp = self.num_to_col(self.col_to_num(start[0]) - 1) + start[1:]
                result = board_object.get_space_info(temp)
                if result is not None and result.get_color() != self.get_color():
                    potential_moves.append(temp)
                elif result is None:
                    potential_moves.append(temp)
                if self.col_to_num(start[0]) + 1 <= 9:
                    temp = self.num_to_col(self.col_to_num(start[0]) + 1) + start[1:]
                    result = board_object.get_space_info(temp)
                    if result is not None and result.get_color() != self.get_color():
                        potential_moves.append(temp)
                    elif result is None:
                        potential_moves.append(temp)
                if int(start[1]) - 1 >= 1:
                    temp = start[0] + str(int(start[1]) - 1)
                    result = board_object.get_space_info(temp)
                    if result is not None and result.get_color() != self.get_color():
                        potential_moves.append(temp)
                    elif result is None:
                        potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
