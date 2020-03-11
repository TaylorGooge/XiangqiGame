from baseclasses import Piece

class Elephant(Piece):
    """
    This class inherits from the Piece class and instantiates a General object.
    """

    def __init__(self, color, location):
        """
        Applies the Piece class init and also initializes title, location, and possible moves data members.
        :param color: Red or Black
        :param location: The space the piece occupies on the board, if any.
         """
        self._title = "E"
        super().__init__(color, location)

    def get_title(self):
        """
        This is a getter function that returns the title of the General object.
        :return: title of the general object.
        """
        return self._title

    def elephant_river_cross_check(self, end):
        """
        This function determines whether the elephant has crossed the "river".
        :param end: Where the elephant will move to.
        :return: True/ False
        """
        if self.get_color() == "red":
            temp_move_value = int(end[1:]) <= 5
            if temp_move_value is not True:
                return False
            else:
                return True
        elif self.get_color() == "black":
            temp_move_value = int(end[1:]) >= 6
            if temp_move_value is not True:
                return False
            else:
                return True

    def elephant_move_check(self, end, board_object, temp_end_obj):
        """
        This function determines whether the passed start and end values constitute a valid diagonal and unblocked move.
        :param temp_end_obj: The piece occupying the ending space, if any.
        :param end: The space to move the Elephant to
        :param board_object: The board object
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
        At the conclusion of a valid move the elephant's spaces attacked are updated.
        :param board_object: The board class object.
        :param end: The space the piece moved into at the conclusion of a valid move.
        :return: None
        """

        potential_moves = []
        start = end

        # 2,-2
        temp = self.col_to_num(start[0]) + 2
        if temp <= 9 and int(start[1:]) - 2 >= 1:
            temp = self.num_to_col(temp) + str(int(start[1:]) - 2)
            temp_obj = board_object.get_space_info(temp)
            if self.elephant_river_cross_check(temp) is True:
                if temp_obj is None or temp_obj.get_color() != self.get_color():
                    potential_moves.append(temp)
        # -2,-2
        temp = self.col_to_num(start[0]) - 2
        if temp >= 1 and int(start[1:]) - 2 >= 1:
            temp = self.num_to_col(temp) + str(int(start[1:]) - 2)
            temp_obj = board_object.get_space_info(temp)
            if self.elephant_river_cross_check(temp) is True:
                if temp_obj is None or temp_obj.get_color() != self.get_color():
                    potential_moves.append(temp)
        # -2,2
        temp = self.col_to_num(start[0]) - 2
        if temp >= 1 and int(start[1:]) + 2 <= 10:
            temp = self.num_to_col(temp) + str(int(start[1:]) + 2)
            temp_obj = board_object.get_space_info(temp)
            if self.elephant_river_cross_check(temp) is True:
                if temp_obj is None or temp_obj.get_color() != self.get_color():
                    potential_moves.append(temp)
        # 2,2
        temp = self.col_to_num(start[0]) + 2
        if temp <= 9 and int(start[1:]) + 2 <= 10 and int(start[1:]) + 2 <= 10:
            temp = self.num_to_col(temp) + str(int(start[1:]) + 2)
            temp_obj = board_object.get_space_info(temp)
            if self.elephant_river_cross_check(temp) is True:
                if temp_obj is None or temp_obj.get_color() != self.get_color():
                    potential_moves.append(temp)

        self.update_potential_moves(potential_moves)
