from baseclasses import Piece


class Horse(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, potential moves, and block spaces
        data members.
        :param color: Red or Black
        :param location: The space the piece occupies, if any.
        """
        self._title = "H"
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

    def horse_move_check(self, end, board_object, temp_end_obj):
        """
        This function determines whether the passed start and end values constitute a valid move.
        :param board_object: The board class object.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The space to move the Horse.
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
        At the conclusion of a valid move the pieces potential moves are updated to the current attacked spaces.
        :param board_object: The board class object.
        :param end: The space the horse moved to at the conclusion of the player's last turn.
        :return: None
        """

        potential_moves = []
        start = end

        # 2,1
        temp = self.col_to_num(start[0]) + 2
        if 1 <= temp <= 9 and int(start[1:]) + 1 < 11:
            temp = self.num_to_col(temp) + str(int(start[1:]) + 1)
            block_space = self.num_to_col(self.col_to_num(start[0]) + 1) + start[1:]
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)

        # 2,-1
        temp = self.col_to_num(start[0]) + 2
        block_space = self.col_to_num(start[0]) + 1
        if 1 <= block_space <= 8 and 1 <= temp <= 9 and int(end[1:]) - 1 > 0:
            block_space = self.num_to_col(block_space) + start[1:]
            temp = self.num_to_col(temp) + str(int(end[1:]) - 1)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)
        # -2,1
        temp = self.col_to_num(start[0]) - 2
        block_space = self.col_to_num(start[0]) + 1
        if 1 <= block_space <= 8 and temp >= 1 and int(start[1:]) + 1 < 11:
            block_space = self.num_to_col(block_space) + start[1:]
            temp = self.num_to_col(temp) + str(int(end[1:]) + 1)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)
        # -2,-1
        temp = self.col_to_num(start[0]) - 2
        block_space = self.col_to_num(start[0]) - 1
        if block_space >= 1 and temp >= 1 and int(end[1:]) - 1 > 0:
            block_space = self.num_to_col(block_space) + start[1:]
            temp = self.num_to_col(temp) + str(int(end[1:]) - 1)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)
        # 1,2
        temp = self.col_to_num(start[0]) + 1
        block_space = start[0] + str(int(start[1:]) + 1)
        if 1 <= temp <= 9 and int(end[1:]) + 2 <= 10:
            temp = self.num_to_col(temp) + str(int(end[1:]) + 2)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)
        # 1,-2
        temp = self.col_to_num(start[0]) + 1
        block_space = int(start[1:]) - 1
        end = int(end[1:]) - 2
        if block_space >= 1 and 1 <= temp <= 9 and end >= 1:
            block_space = start[0] + str(block_space)
            temp = self.num_to_col(temp) + str(end)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)
        # -1,-2
        temp = self.col_to_num(start[0]) - 1
        block_space = int(start[1:]) - 1
        end = int(start[1:]) - 2
        if block_space > 0 and temp >= 1 and 1 <= end <= 10:
            block_space = start[0] + str(block_space)
            temp = self.num_to_col(temp) + str(end)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is None:
                if board_object.get_space_info(block_space) is not None:
                    pass
                else:
                    if temp_obj is None or temp_obj.get_color != self.get_color():
                        potential_moves.append(temp)

        # -1,2
        temp = self.col_to_num(start[0]) - 1
        block_space = int(start[1:]) + 1
        if 1 <= block_space <= 10 and temp >= 1 and int(start[1:]) + 2 <= 10:
            block_space = start[0] + str(block_space)
            temp = self.num_to_col(temp) + str(int(start[1:]) + 2)
            temp_obj = board_object.get_space_info(temp)
            if board_object.get_space_info(block_space) is not None:
                pass
            else:
                if temp_obj is None or temp_obj.get_color != self.get_color():
                    potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
