from baseclasses import Piece, Error, InvalidMoveError
from general import General
from chariot import Chariot
from horse import Horse
from elephant import Elephant
from advisor import Advisor
from cannon import Cannon
from soldier import Soldier



def main():
    pass


class XiangqiGame:
    """
    This class contains the board game  and all functions necessary for the board to function during a game.
    """

    def __init__(self):
        """
        This constructor instantiates a game board, instantiates and adds the game piece objects to the board,
        initializes the game state to "unfinished",  initializes the current turn as the red players,
        and initializes the in-check status of the players.
        """
        self._board = self._board = {"a1": None, "b1": None, "c1": None, "d1": None, "e1": None, "f1": None, "g1": None,
                                     "h1": None, "i1": None,
                                     # row 2
                                     "a2": None, "b2": None, "c2": None, "d2": None, "e2": None, "f2": None, "g2": None,
                                     "h2": None, "i2": None,
                                     # row 3
                                     "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None,
                                     "h3": None, "i3": None,
                                     # row 4
                                     "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None,
                                     "h4": None, "i4": None,
                                     # row 5
                                     "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None,
                                     "h5": None, "i5": None,
                                     # row 6
                                     "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None,
                                     "h6": None, "i6": None,
                                     # row 7
                                     "a7": None, "b7": None, "c7": None, "d7": None, "e7": None, "f7": None, "g7": None,
                                     "h7": None, "i7": None,
                                     # row 8
                                     "a8": None, "b8": None, "c8": None, "d8": None, "e8": None, "f8": None, "g8": None,
                                     "h8": None, "i8": None,
                                     # row 9
                                     "a9": None, "b9": None, "c9": None, "d9": None, "e9": None, "f9": None, "g9": None,
                                     "h9": None, "i9": None,
                                     # row 10
                                     "a10": None, "b10": None, "c10": None, "d10": None, "e10": None, "f10": None,
                                     "g10": None, "h10": None, "i10": None,
                                     }
        self._red_pieces = []
        self._black_pieces = []

        red_char_1 = Chariot("red", "a1")
        self.update_board("a1", red_char_1)
        self._red_pieces.append(red_char_1)

        black_char_1 = Chariot("Black", "a10")
        self.update_board("a10", black_char_1)
        self._black_pieces.append(black_char_1)

        red_horse_1 = Horse("red", "b1")
        self.update_board("b1", red_horse_1)
        self._red_pieces.append(red_horse_1)

        black_horse_1 = Horse("black", "b10")
        self.update_board("b10", black_horse_1)
        self._black_pieces.append(black_horse_1)

        red_ele_1 = Elephant("red", "c1")
        self.update_board("c1", red_ele_1)
        self._red_pieces.append(red_ele_1)

        black_ele_1 = Elephant("black", "c10")
        self.update_board("c10", black_ele_1)
        self._black_pieces.append(black_ele_1)

        red_adv_1 = Advisor("red", "d1")
        self.update_board("d1", red_adv_1)
        self._red_pieces.append(red_adv_1)

        black_adv_1 = Advisor("black", "d10")
        self.update_board("d10", black_adv_1)
        self._black_pieces.append(black_adv_1)

        red_gen = General("red", "e1")
        self.update_board("e1", red_gen)
        self._red_pieces.append(red_gen)

        black_gen = General("Black", "e10")
        self.update_board("e10", black_gen)
        self._black_pieces.append(black_gen)

        red_adv_2 = Advisor("Red", "f1")
        self.update_board("f1", red_adv_2)
        self._red_pieces.append(red_adv_2)

        black_adv_2 = Advisor("black", "f10")
        self.update_board("f10", black_adv_2)
        self._black_pieces.append(black_adv_2)

        red_ele_2 = Elephant("red", "g1")
        self.update_board("g1", red_ele_2)
        self._red_pieces.append(red_ele_2)

        black_ele_2 = Elephant("black", "g10")
        self.update_board("g10", black_ele_2)
        self._black_pieces.append(black_ele_2)

        red_horse_2 = Horse("red", "h1")
        self.update_board("h1", red_horse_2)
        self._red_pieces.append(red_horse_2)

        black_horse_2 = Horse("black", "h10")
        self.update_board("h10", black_horse_2)
        self._black_pieces.append(black_horse_2)

        red_char_2 = Chariot("red", "i1")
        self.update_board("i1", red_char_2)
        self._red_pieces.append(red_char_2)

        black_char_2 = Chariot("black", "i10")
        self.update_board("i10", black_char_2)
        self._black_pieces.append(black_char_2)

        red_can_1 = Cannon("red", "b3")
        self.update_board("b3", red_can_1)
        self._red_pieces.append(red_can_1)

        black_can_1 = Cannon("black", "b8")
        self.update_board("b8", black_can_1)
        self._black_pieces.append(black_can_1)

        red_can_2 = Cannon("red", "h3")
        self.update_board("h3", red_can_2)
        self._red_pieces.append(red_can_2)

        black_can_2 = Cannon("black", "h8")
        self.update_board("h8", black_can_2)
        self._black_pieces.append(black_can_2)

        red_sol_1 = Soldier("red", "a4")
        self.update_board("a4", red_sol_1)
        self._red_pieces.append(red_sol_1)

        red_sol_2 = Soldier("red", "c4")
        self.update_board("c4", red_sol_2)
        self._red_pieces.append(red_sol_2)

        red_sol_3 = Soldier("red", "e4")
        self.update_board("e4", red_sol_3)
        self._red_pieces.append(red_sol_3)

        red_sol_4 = Soldier("red", "g4")
        self.update_board("g4", red_sol_4)
        self._red_pieces.append(red_sol_4)

        red_sol_5 = Soldier("red", "i4")
        self.update_board("i4", red_sol_5)
        self._red_pieces.append(red_sol_5)

        black_sol_1 = Soldier("black", "a7")
        self.update_board("a7", black_sol_1)
        self._black_pieces.append(black_sol_1)

        black_sol_2 = Soldier("black", "c7")
        self.update_board("c7", black_sol_2)
        self._black_pieces.append(black_sol_2)

        black_sol_3 = Soldier("black", "e7")
        self.update_board("e7", black_sol_3)
        self._black_pieces.append(black_sol_3)

        black_sol_4 = Soldier("black", "g7")
        self.update_board("g7", black_sol_4)
        self._black_pieces.append(black_sol_4)

        black_sol_5 = Soldier("black", "i7")
        self.update_board("i7", black_sol_5)
        self._black_pieces.append(black_sol_5)

        self._game_state = "UNFINISHED"
        self._turn = True

        self.generate_moves()

        self._red_in_check = {"red": False, "object": None}
        self._black_in_check = {"black": False, "object": None}

    def generate_moves(self):
        """
        This function generates all potential moves each player can make.
        :return: None
        """
        for pieces in self._red_pieces:
            pieces.possible_moves(self, pieces.get_location())
        for pieces in self._black_pieces:
            pieces.possible_moves(self, pieces.get_location())

    def get_red_pieces(self):
        """
        This function returns all of the pieces that belong to the red player.
        """
        return self._red_pieces

    def get_black_pieces(self):
        """
        This function returns all of the pieces that belong to the black player.
        :return:
        """
        return self._black_pieces

    def update_pieces_list(self, obj):
        """
        The function removes a piece from the player's piece list when it captured by the opponent.
        :param obj: The piece to be removed.
        :return: None
        """
        remove_obj = self.get_space_info(obj)

        if remove_obj is not None:
            temp_color = remove_obj.get_color()
            if temp_color == "red":
                for i in self._red_pieces:
                    if i is remove_obj:
                        remove_obj.update_location(None)
                        self._red_pieces.remove(i)
            elif temp_color == "black":
                for i in self._black_pieces:
                    if i is remove_obj:
                        remove_obj.update_location(None)
                        self._black_pieces.remove(i)

    def get_space_info(self, location):
        """
        This function returns which piece is located on the passed space, if any.
        :param location: Location on the board.
        :return: Piece object or None
        """
        return self._board[location]

    def update_board(self, location, value):
        """
        This function updates the passed board location with the passed piece object.
        :param location: The location to be updated.
        :param value: The Piece object or None
        :return: None
        """
        self._board[location] = value

    def get_game_state(self):
        """
        This function returns the current state of the game.
        :return: UNFINISHED, RED_WON, BLACK_WON
        """
        return self._game_state

    def update_game_state(self, value):
        """
        This function updates the game state.
        :param value: RED_WON, BLACK_WON
        :return: None
        """
        self._game_state = value

        if self._game_state != "UNFINISHED":
            return self._game_state

    def get_board(self):
        """
        This function returns the board
        :return: the game board
        """
        return self._board

    def update_in_check(self, color, value, game_space):
        """
        When in it is determined that a player is in check this function is called to update the in_check dictionary
        :return: None
        """
        if color == "red":
            self._red_in_check = {"red": value, "object": game_space}
        elif color == "black":
            self._black_in_check = {"black": value, "object": game_space}

    def is_in_check(self, player):
        """
        This function returns whether any player is currently in check.
        :param player: red/black
        :return: True, False
        """
        if player == "red":
            return self._red_in_check["red"]
        elif player == "black":
            return self._black_in_check["black"]
        else:
            return "Invalid player"

    def get_in_check_dicts(self, player):
        """
        This function returns the entirety of the in_check_dict for the passed player.
        :param player: red/black
        """
        if player == "red":
            return self._red_in_check
        elif player == "black":
            return self._black_in_check
        else:
            return "Invalid player"

    def move_except(self, start, end):
        """
        This check validates that the start and end locations are valid.
        :param start: The start start space
        :param end: The end space
        :return: True / False
        """
        valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        valid_rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valid_rows = [str(num) for num in valid_rows]
        start_col = start[0]
        start_row = str(start[1:])
        end_col = end[0]
        end_row = str(end[1:])

        if start_col in valid_columns:
            if start_row in valid_rows:
                if end_col in valid_columns:
                    if end_row in valid_rows:
                        return True

    def get_turn(self):
        """
        This function returns which player may take a turn
        :return: True(red), False(black)
        """
        return self._turn

    def update_turn(self):
        """
       After the completion of a valid move, this function is called to update which player may take a turn next.
       :return: None
        """
        if self.get_turn() is True:
            self._turn = False
        elif self.get_turn() is False:
            self._turn = True

    def turn_validation(self, temp_start_object):
        """
        This function validates whether the current player may take a turn
        :param temp_start_object: The object to try to move
        :return: True/False
        """

        if self.get_turn() is True:
            if temp_start_object.get_color() == "red":
                return True
            else:
                return False
        elif self.get_turn() is False:
            if temp_start_object.get_color() == "black":
                return True
            else:
                return False

    def declare_winner(self, temp_color):
        """
        This function updates the game state when a player has won
        :param temp_color: The color of the piece in check
        :return: None
        """
        if temp_color == "red":
            self.update_game_state("BLACK_WON")
            return
        else:
            self.update_game_state("RED_WON")
            return

    def out_of_check(self, temp_color):
        """
        This function takes a player out of check when possible.
        :param temp_color: The color of the piece in check
        :return: None
        """
        if temp_color == "red":
            self.update_in_check("red", False, None)
            return
        else:
            self.update_in_check("black", False, None)
            return

    def stalemate(self):
        """
        This function declares a stalemate when there are not valid moves but no player is in check.
        :return: None
        """
        if self.is_in_check("black") is False:
            black_moves = []
            for piece in self.get_black_pieces():
                for move in piece.get_potential_moves():
                    black_moves.append(move)
            if len(black_moves) == 0:
                if self.get_turn() == "True":
                    self.update_game_state("RED_WON")
                else:
                    self.update_game_state("BLACK_WON")
        elif self.is_in_check("red") is False:
            red_moves = []
            for piece in self.get_red_pieces():
                for move in piece.get_potential_moves():
                    red_moves.append(move)
            if len(red_moves) == 0:
                if self.get_turn() == "True":
                    self.update_game_state("RED_WON")
                else:
                    self.update_game_state("BLACK_WON")

    def in_check_determine(self):
        """
        If a player can be captured during their next move this function moves the player into check.
        :return: None
        """
        for piece in self.get_red_pieces():
            for moves in piece.get_potential_moves():
                if self.get_space_info(moves) is None:
                    pass
                else:
                    result = self.get_space_info(moves)
                    if result.get_title() == "G" and result.get_color() == "black":
                        self.update_in_check("black", True, piece.get_location())
                        print("Black player is in check")
        for piece in self.get_black_pieces():
            for moves in piece.get_potential_moves():
                if self.get_space_info(moves) is None:
                    pass
                else:
                    result = self.get_space_info(moves)
                    if result.get_title() == "G" and result.get_color() == "red":
                        self.update_in_check("red", True, piece.get_location())
                        print("Red player is in check")

    def avoid_check_mate(self):
        """
        This function determines whether a player can avoid check-mate.
        :return: The game state is either updated to reflect a win, or the in-check status is updated and the game
        continues.
        """
        beat_check = False

        if self.is_in_check("red") is True:
            temp_color = "red"
            for pieces in self.get_red_pieces():
                for moves in pieces.get_potential_moves():
                    if self.get_space_info(moves) is None:
                        self.out_of_check(temp_color)
                        self.update_board(moves, pieces)
                        self.generate_moves()
                        self.in_check_determine()
                        if self.is_in_check(temp_color) is False:
                            beat_check = True
                            self.update_board(moves, None)
                        else:
                            self.update_board(moves, None)
            if beat_check is True:
                self.out_of_check(temp_color)
                self.generate_moves()
            else:
                self.declare_winner(temp_color)
        elif self.is_in_check("black") is True:
            temp_color = "black"
            for pieces in self.get_black_pieces():
                for moves in pieces.get_potential_moves():
                    if self.get_space_info(moves) is None:
                        self.out_of_check(temp_color)
                        self.update_board(moves, pieces)
                        self.generate_moves()
                        self.in_check_determine()
                        if self.is_in_check(temp_color) is False:
                            beat_check = True
                            self.update_board(moves, None)
                        else:
                            self.update_board(moves, None)
            if beat_check is True:
                self.out_of_check(temp_color)
                self.generate_moves()
            else:
                self.declare_winner(temp_color)

    def make_move_helper(self, start, end, temp_start_obj):
        """
        When a valid move is determined this function updates the board, updates the turn, generates all possible moves
        for pieces on the board, determined if the player is in check, stalemate, and can avoid checkmate.
        :param start: The start position of the valid move.
        :param end: The end position of the valid move.
        :param temp_start_obj: The piece object to move.
        :return: None
        """
        self.update_board(start, None)
        self.update_board(end, temp_start_obj)
        temp_start_obj.update_location(end)
        self.update_turn()
        self.generate_moves()
        self.in_check_determine()
        self.stalemate()
        self.avoid_check_mate()

    def make_move(self, start, end):
        """
        This function initiates a proposed move.
        :param start: The start position of the valid move.
        :param end: The end position of the valid move.
        :return: True/Fa;se
        """
        temp_start_obj = self.get_space_info(start)
        temp_end_obj = self.get_space_info(end)
        temp_type = temp_start_obj.get_title()
        board_object = self

        if self.turn_validation(temp_start_obj) is False:
            return "It is not your turn"

        if self.move_except(start, end) is not True:
            raise InvalidMoveError("Try a valid algebraic notation input")

        if self.get_game_state() != "UNFINISHED":
            return "Game Over"
        else:
            if temp_type == "E":
                if temp_start_obj.elephant_move_check(end, board_object,
                                                      temp_end_obj) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Elephant move"
            elif temp_type == "A":
                if temp_start_obj.advisor_move_check(end, temp_end_obj,
                                                     board_object) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Advisor move"
            elif temp_type == "G":
                if temp_start_obj.general_move_check(start, end, board_object,
                                                     temp_end_obj) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid General move"
            elif temp_type == "C":
                if temp_start_obj.chariot_move_check(end, board_object,
                                                     temp_end_obj) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Chariot move"
            elif temp_type == "H":
                if temp_start_obj.horse_move_check(end, board_object,
                                                   temp_end_obj) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Horse move"
            elif temp_type == "S":
                if temp_start_obj.soldier_move_check(end, temp_end_obj,
                                                     board_object) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Soldier move"
            elif temp_type == "Can":
                if temp_start_obj.cannon_move_check(end, board_object,
                                                    temp_end_obj) is True:
                    self.make_move_helper(start, end, temp_start_obj)
                    return True
                else:
                    return "That is not a valid Cannon move"


if __name__ == "__main__":
    main()
