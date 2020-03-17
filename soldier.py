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
        before_river_allowable_moves= [(0,1)]
        after_river_allowable_moves = [(0,1), (1,0), (-1,0)]
        potential_moves = []
        start = end

        if self.get_color() == "red":
            if int(start[1:]) <= 5:
                for moves in before_river_allowable_moves:
                    if 1 <= int(start[1:]) + moves[1] <= 10:
                        temp = start[0] + str(int(start[1:]) + moves[1])
                        temp_obj = board_object.get_space_info(temp)
                        if temp_obj is None or temp_obj.get_color() != self.get_color() :
                            potential_moves.append(temp)
            else:
                for moves in after_river_allowable_moves:
                    if 1 <= int(start[1:]) + moves[1] <= 10 and 1<= self.col_to_num(start[0]) + moves[0] <= 9:
                        temp = self.num_to_col(self.col_to_num(start[0]) + moves[0])+ str(int(start[1:]) + moves[1])
                        temp_obj = board_object.get_space_info(temp)
                        if temp_obj is None or temp_obj.get_color() != self.get_color():
                            potential_moves.append(temp)
        elif self.get_color() == "black":
            if int(start[1:]) >= 6:
                for moves in before_river_allowable_moves:
                    if 1<= int(start[1:]) + -(moves[1]) <=10:
                        temp = start[0] + str(int(start[1:]) + -(moves[1]))
                        temp_obj = board_object.get_space_info(temp)
                        if temp_obj is None or temp_obj.get_color() != self.get_color():
                            potential_moves.append(temp)
            else:
                for moves in after_river_allowable_moves:
                    if 1 <= int(start[1:]) + -(moves[1]) <= 10 and 1 <= self.col_to_num(start[0]) + -(moves[0]) <= 9:
                        temp = self.num_to_col(self.col_to_num(start[0]) + moves[0]) + str(int(start[1:]) + -(moves[1]))
                        temp_obj = board_object.get_space_info(temp)
                        if temp_obj is None or temp_obj.get_color() != self.get_color() :
                            potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
