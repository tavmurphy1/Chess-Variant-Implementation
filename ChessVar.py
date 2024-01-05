# Author: Tavner Murphy
# GitHub username: tavmurphy1
# Date: 12/10/23
# Description: Contains a series of classes representing a playable variant of Chess, in which
# a player of white or black teams wins by capturing all the pieces of one TYPE of chess
# piece belonging to the opposing player.

class ChessVar:
    """
    Represents an abstract game of a chess variant with White and Black teams. A player wins by capturing all the pieces
     of one type of piece belonging to the opposing player. Communicates with Piece class and subclasses to initialize
     board and make valid moves.

    Contains the following data members:
        -game_state: the current game state
        -current_turn: whose player's turn it is
        -board: a list of dictionaries representing 8x8 squares and their Piece occupants
        -white_pieces: a dictionary containing a running count of white pieces remaining, by type
        -black_pieces: same as white_pieces but for black pieces

    Contains the following methods:
        -make_move: moves a piece from one square to another if and only if the movement is valid. Returns 'True' if the
         move is valid and successfully completed and 'False' if the move is invalid. Communicates with Piece
         class/subclasses to determine if moves are valid.

        -get_game_state: returns the game state, ('UNFINISHED', 'WHITE_WON', or 'BLACK_WON').
        -get_current_turn: returns the player whose turn it currently is
        -get_board: returns a representation of the current board state.
        -get_white_pieces_remaining: returns the dictionary containing counts of white pieces remaining
        -get_black_pieces_remaining: returns the dictionary containing counts of black pieces remaining
    """

    def __init__(self):
        """
        Initializes a chess game with 'UNFINISHED' game state, 'WHITE' as current player, and a list of dictionaries
        representing a chess board with 8x8 squares. It then populates those squares with Piece objects according to
        piece starting positions in Chess
        """

        self._game_state = 'UNFINISHED'
        self._current_player = 'WHITE'
        self._board = {
            'A': {'8': Rook('BLACK', 'A8'), '7': Pawn('BLACK', 'A7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'A2'), '1': Rook('WHITE', 'A1')},

            'B': {'8': Knight('BLACK', 'B8'), '7': Pawn('BLACK', 'B7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'B2'), '1': Knight('WHITE', 'B1')},

            'C': {'8': Bishop('BLACK', 'C8'), '7': Pawn('BLACK', 'C7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'C2'), '1': Bishop('WHITE', 'C1')},

            'D': {'8': Queen('BLACK', 'D8'), '7': Pawn('BLACK', 'D7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'D2'), '1': Queen('WHITE', 'D1')},

            'E': {'8': King('BLACK', 'E8'), '7': Pawn('BLACK', 'E7'), '6': None, '5': None, '4': None, '3': None,

                  '2': Pawn('WHITE', 'E2'), '1': King('WHITE', 'E1')},

            'F': {'8': Bishop('BLACK', 'F8'), '7': Pawn('BLACK', 'F7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'F2'), '1': Bishop('WHITE', 'F1')},

            'G': {'8': Knight('BLACK', 'G8'), '7': Pawn('BLACK', 'G7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'G2'), '1': Knight('WHITE', 'G1')},

            'H': {'8': Rook('BLACK', 'H8'), '7': Pawn('BLACK', 'H7'), '6': None, '5': None, '4': None, '3': None,
                  '2': Pawn('WHITE', 'H2'), '1': Rook('WHITE', 'H1')}
        }

        self._white_pieces = {'Pawn': 8, 'Rook': 2, 'Knight': 2, 'Bishop': 2, 'Queen': 1, 'King': 1}
        self._black_pieces = {'Pawn': 8, 'Rook': 2, 'Knight': 2, 'Bishop': 2, 'Queen': 1, 'King': 1}

    def get_game_state(self):
        """
        Returns the current state of the game: White wins if the board has 0 pieces of one type of black piece and vice
        versa, and the game is unfinished if both teams still have at least one piece of each type on the board.

        Input: No parameters

        Return: One of the values('UNFINISHED', 'WHITE_WON', or 'BLACK_WON')
        """

        return self._game_state

    def get_board(self):
        """
        Returns a representation of the board state.

        Input: No parameters

        Returns: 'Board' data member
        """

        return self._board

    def get_current_turn(self):
        """
        Returns whose players turn it is.

        Input: No parameters.

        Returns: 'WHITE' or 'BLACK'
        """
        return self._current_player

    def get_white_pieces_remaining(self):
        """
        Returns the dictionary of remaining white pieces in the game.
        """
        return self._white_pieces

    def get_black_pieces_remaining(self):
        """
        Returns the dictionary of remaining black pieces in the game
        """
        return self._black_pieces

    def make_move(self, from_square, to_square):
        """
        Updates the board with a single move, moving a piece from the square it is currently occupying to a different
        valid square, validity determined according to that piece's movement rules and whose turn it is. If there is a
        piece belonging to the opposing team in the moved piece's final space, it is 'taken' and overwritten. The
        function then checks if the game has been won by either player and updates the game state accordingly.

        Communicates with all Piece subclasses to determine move validity.

        Inputs: 2x strings representing square moved from,
         and square moved to, respectively

        Returns:
               'False' if
                1. The square being moved from does not contain
                a piece belonging to the player whose turn it is.
                2. The indicated move is not legal.
                3. The game has already been won.

                'True' if:
                1. The move is valid and board/game state
                and turn order have updated successfully.
        """

        print(f"from_square is {from_square} and to_square is {to_square}")

        possible_rows = ('1', '2', '3', '4', '5', '6', '7', '8')
        possible_columns = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

        # 1. Convert to uppercase
        from_square = str(from_square.upper())
        to_square = str(to_square.upper())

        # 2. Handle inputs are the same
        if from_square == to_square:
            print("ERROR: Movement parameters cannot be the same.Try again!\n")
            return False

        # 3. Handle incorrect entry size
        if len(from_square) != 2 or len(to_square) != 2:
            print("ERROR: Movement parameters must be entered in algebraic notation. Try again!\n")
            return False

        # 4. Handle incorrect numbers/letters
        column1 = from_square[0]
        row1 = from_square[1]

        column2 = to_square[0]
        row2 = to_square[1]

        if (row1 not in possible_rows) or (column1 not in possible_columns):
            print("ERROR: Movement parameters provided for from_square must be in 'column + row' algebraic notation\n"
                  " where 'column' is a  letter 'A-H' and 'row' is a number '1-8'. Try again!\n")
            return False

        if (row2 not in possible_rows) or (column2 not in possible_columns):
            print("ERROR: Movement parameters provided for to_square must be in 'column + row' algebraic notation\n"
                  " where 'column' is a letter 'A-H' and 'row' is a number '1-8'. Try again!\n")
            return False

        # 5. Handle trying to move when game already won
        if self._game_state != 'UNFINISHED':
            print("ERROR: You are trying to move when one team has already won. Try starting a new game!\n")
            return False

        from_square_piece = self._board[column1][row1]
        to_square = self._board[column2][row2]

        to_square_string = column2 + row2

        # 6. Handle trying to move from empty square
        if from_square_piece is None:
            print("Error: You are trying to move a piece from an empty square. Try again.\n")
            return False

        # 7. Handle trying to move other teams piece
        if from_square_piece.get_team() != self._current_player:
            print("Error: It is not your turn or you are trying to move a piece belonging to the other team.\n"
                  "Try again.\n")
            return False

        # 8. Handle incorrect movement rules
        if not from_square_piece.is_valid_move(to_square_string, self.get_board()):
            print("Error: Your move does not follow correct movement rules for that type of piece. Try again.\n")
            return False

        # 9. Handle trying to move to a square occupied by same team
        if to_square is not None:
            if to_square.get_team() == self._current_player:
                print("Error: You are trying to move your piece on to a square that is already occupied by a piece \n"
                      "of your team's color. Try again.\n")
                return False
            # 10a. If the to square is occupied enemy piece, capture
            else:
                if to_square.get_team() == 'BLACK':
                    print(to_square.get_team() + " " + to_square.get_type() + " " + "captured.\n")
                    self._black_pieces[to_square.get_type()] -= 1

                    # 10b update board and piece position
                    self._board[column2][row2] = from_square_piece
                    from_square_piece.set_position(to_square_string)

                elif to_square.get_team() == 'WHITE':
                    print(to_square.get_team() + " " + to_square.get_type() + " " + "captured.\n")
                    self._white_pieces[to_square.get_type()] -= 1

                    # 10b update board and position
                    self._board[column2][row2] = from_square_piece
                    from_square_piece.set_position(to_square_string)

        # 11. If no capture but valid move, update position for Piece object
        elif to_square is None:
            from_square_piece.set_position(to_square_string)

        # 12. If Pawn, set has_moved to 'True'
        if from_square_piece.get_type() == 'Pawn':
            if from_square_piece.get_has_moved() is False:
                from_square_piece.set_has_moved()

        # 13. Update the board
        self._board[column2][row2] = from_square_piece
        self._board[column1][row1] = None

        # 14. Check if game has been won, then update turn order, return True
        if self._current_player == 'WHITE':
            if 0 in self._black_pieces.values():
                self._game_state = 'WHITE_WON'
                print(self._game_state)
                return True
            else:
                self._current_player = 'BLACK'
                return True

        if self._current_player == 'BLACK':
            if 0 in self._white_pieces.values():
                self._game_state = 'BLACK_WON'
                print(self._game_state)
                return True
            else:
                self._current_player = 'WHITE'
                return True


class Piece:
    """
    Represents a piece in abstract game of chess
    """

    def __init__(self, team, position):
        """
        Initializes chess piece with a team, type, and starting position
        """
        self._team = team
        self._position = position
        self._column = position[0]
        self._row = position[1]

    def get_team(self):
        """
        Returns 'BLACK' or 'WHITE'
        """
        return self._team

    def get_position(self):
        """
        Returns current position on the board
        """
        return self._position

    def set_position(self, position):
        """
        Sets a new position for the piece
        """
        self._position = position
        self._column = position[0]
        self._row = position[1]

    def get_row(self):
        """
        Returns the row the piece is in as a numeric Char
        """
        return self._row

    def get_column(self):
        """
        Returns the column the piece is in as a capital Char
        """
        return self._column

    def get_type(self):
        """
        Returns the subclass of the piece,
        """
        return self._type


class Pawn(Piece):
    """
    Represents a type of piece that moves up to two spaces forward the first time it is moved and only one space forward
    thereafter. It can capture other pieces by moving diagonally forward.

    Column, row, type data members and a special has_moved data member
    """

    def __init__(self, team, position):
        """
        Initializes a pawn with its team and starting board position.
        """
        super().__init__(team, position)

        self._column = position[0]
        self._row = position[1]
        self._type = 'Pawn'

        # data member to tell if pawn has taken first move
        self._has_moved = False

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for Pawn. Returns true is valid, false if invalid
        """

        row1 = self._row
        column1 = self._column

        column2 = move_to[0]
        row2 = move_to[1]

        has_moved = self._has_moved
        team = self._team

        if column1 != column2:
            if board[column2][row2] is None:
                print("Error: Pawn cannon move diagonally except to capture. Try again.\n")
                return False
            # Handle attempted capture by moving forward
        if column1 == column2:
            if board[column2][row2] is not None:
                print("Error: Pawn cannot capture by moving forward. Try again.\n")
                return False
        elif self.get_team() == 'WHITE':
            if row2 == str(int(row1) + 2):
                if board[column1][str(int(row1) + 1)] is not None:
                    print("Error: Movement blocked. Try again.\n")
                    return False
                elif board[column1][str(int(row1) + 2)] is not None:
                    print("Error: Movement blocked. Try again.\n")
                    return False

        elif self.get_team() == 'BLACK':
            if row2 == str((int(row1) - 2)):
                if board[column1][str(int(row1) - 1)] is not None:
                    print("Error: Movement blocked. Try again.\n")
                    return False

                elif board[column1][str(int(row1) - 2)] is not None:
                    print("Error: Movement blocked. Try again.\n")
                    return False

            # If pawn has not yet moved it can move two spaces
        if team == 'WHITE':
            if has_moved is False:
                white_valid_rows = ['3', '4']
                white_valid_columns = [column1, chr(ord(column1) + 1), chr(ord(column1) - 1)]
                if row2 == '4':
                    white_valid_columns = [column1]
                if (row2 in white_valid_rows) and (column2 in white_valid_columns):
                    self._has_moved = True
                    return True

            # If pawn has already moved it can move 1 space
            elif has_moved is True:
                white_valid_rows = [str(int(row1) + 1)]
                white_valid_columns = [column1, chr(ord(column1) + 1), chr(ord(column1) - 1)]
                if (row2 in white_valid_rows) and (column2 in white_valid_columns):
                    return True

        elif team == 'BLACK':
            if has_moved is False:
                black_valid_rows = ['5', '6']
                black_valid_columns = [column1, chr(ord(column1) + 1), chr(ord(column1) - 1)]
                if row2 == '5':
                    black_valid_columns = [column1]
                if (row2 in black_valid_rows) and (column2 in black_valid_columns):
                    return True

            if has_moved is True:
                black_valid_rows = [str(int(row1) - 1)]
                black_valid_columns = [column1, chr(ord(column1) + 1), chr(ord(column1) - 1)]
                if (row2 in black_valid_rows) and (column2 in black_valid_columns):
                    return True

    def get_has_moved(self):
        """
        Returns whether the Pawn has moved already or not in the game
        """
        return self._has_moved

    def set_has_moved(self):
        """
        Logs whether a Pawn has been moved already
        """
        self._has_moved = True


class Rook(Piece):
    """
    Represents a type of piece that moves in a straight line in cardinal directions any number of spaces or until it is
    blocked by another piece or the edge of the board.
    """

    def __init__(self, team, position):
        """
        Initializes a Rook piece with its team and starting board position.
        """
        super().__init__(team, position)

        self._type = 'Rook'

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for a Rook. Returns true if valid, false if invalid
        """

        column1 = self._column
        row1 = self._row

        column_index = (ord(column1) - 64)
        row_index = int(row1)

        column2 = move_to[0]
        row2 = move_to[1]

        column_difference = abs((ord(column2) - 64) - (ord(column1) - 64))
        row_difference = abs(int(row2) - int(row1))

        # if absolute difference in rows > 0 and difference in columns == 0, the move is vertical
        if row_difference > 0 and column_difference == 0:
            # Moving up
            if row_index < int(row2):
                while row_index < int(row2):
                    row_index += 1
                    if board[column1][str(row_index)] is not None:
                        print("Error: The vertical movement upward is blocked by another piece.")
                        return False
                return True
            # Moving Down
            elif int(row1) > int(row2):
                while row_index > int(row2):
                    row_index -= 1
                    if board[column1][str(row_index)] is not None:
                        print("Error: The vertical movement downward is blocked by another piece.")
                        return False
                return True

        # If the difference in columns > 0 and the difference in rows == 0, the move is horizontal.
        elif column_difference > 0 and row_difference == 0:
            # Moving to the right
            if (ord(column1) - 64) < (ord(column2) - 64):
                while column_index < (ord(column2) - 64):
                    column_index += 1
                    if board[chr(column_index + 64)][row1] is not None:
                        print("Error: The horizontal movement to the right is blocked by another piece.")
                        return False
                return True
            # Moving to the left
            elif (ord(column1) - 64) > (ord(column2) - 64):
                while row_index > int(row2):
                    row_index -= 1
                    if board[str(row_index)][row1] is not None:
                        print("Error: The horizontal movement to the left is blocked by another piece.")
                return True
        else:
            return False


class Knight(Piece):
    """
    Represents a type of piece that moves in an L shape (2-2) in cardinal directions and jumps over any pieces that
    would normally block it. It only takes the piece it lands on.
    """

    def __init__(self, team, position):
        """
        Initializes a Knight piece with its team and starting board position.
        """
        super().__init__(team, position)

        self._type = 'Knight'

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for a kuh-nee-guh-tuh. Returns true if valid, false if invalid
        """

        column1 = self._column
        row1 = self._row

        column2 = move_to[0]
        row2 = move_to[1]

        valid_rows = [str(int(row1) + 1), str(int(row1) + 2), str(int(row1) - 1), str(int(row1) - 2)]
        valid_columns = [chr(ord(column1) + 1), chr(ord(column1) + 2), chr(ord(column1) - 1), chr(ord(column1) - 2)]

        # If moving one row away, column must be 2 rows away and vice versa
        if row2 in valid_rows and column2 in valid_columns:
            if row2 == str(int(row1) + 1) or row2 == str(int(row1) - 1):
                valid_columns2 = [chr(ord(column1) + 2), chr(ord(column1) - 2)]
                if column2 in valid_columns2:
                    return True
                else:
                    return False
            if row2 == str(int(row1) + 2) or row2 == str(int(row1) - 2):
                valid_columns2 = [chr(ord(column1) + 1), chr(ord(column1) - 1)]
                if column2 in valid_columns2:
                    return True
                else:
                    return False
        else:
            return False


class Bishop(Piece):
    """
    Represents a type of piece that moves diagonally any number of spaces or until it is blocked by another piece or the
    edge of the board
    """

    def __init__(self, team, position):
        """
        Initializes a Bishop piece with its team and starting board position.
        """
        super().__init__(team, position)

        self._type = 'Bishop'

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for a King. Returns true if valid, false if invalid
        """

        column1 = self._column
        row1 = self._row

        column2 = move_to[0]
        row2 = move_to[1]

        column_index = (ord(column1) - 64)
        row_index = int(row1)

        column_difference = abs((ord(column2) - 64) - (ord(column1) - 64))
        row_difference = abs(int(row2) - int(row1))

        if column_difference == row_difference:
            # Up and to the right
            if (row_index < int(row2)) and (column_index < (ord(column2) - 64)):
                while row_index < (int(row2) - 1) and column_index < ((ord(column2) - 64) - 1):
                    row_index += 1
                    column_index += 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement is up to the right is blocked by another piece.")
                        return False
                return True
            # Up and to the left
            elif (row_index < int(row2)) and (column_index > (ord(column2) - 64)):
                while row_index < (int(row2) - 1) and (column_index > (ord(column2) - 64) + 1):
                    row_index += 1
                    column_index -= 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement up to the left is blocked by another piece.")
                        return False
                return True
            # Down and to the left
            elif (row_index > int(row2)) and (column_index > (ord(column2) - 64)):
                while row_index > (int(row2) + 1) and (column_index > (ord(column2) - 64) + 1):
                    row_index -= 1
                    column_index -= 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement down and to the left is blocked by another piece.")
                        return False
                return True
            # Down and to the right
            elif (row_index > int(row2)) and (column_index < (ord(column2) - 64)):
                while row_index > (int(row2) + 1) and (column_index < (ord(column2) - 64) - 1):
                    row_index -= 1
                    column_index += 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement down to the right is blocked by another piece.")
                        return False
                return True
        else:
            return False


class Queen(Piece):
    """
    Represents a type of piece that can move in cardinal directions and diagonally, any number of spaces or until
    blocked by another piece or the edge of the board.
    """

    def __init__(self, team, position):
        """
        Initializes a Queen piece with her team and starting board position.
        """
        super().__init__(team, position)

        self._type = 'Queen'

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for a Rook. Returns true if valid, false if invalid
        """

        column1 = self._column
        row1 = self._row

        column2 = move_to[0]
        row2 = move_to[1]

        column_index = (ord(column1) - 64)
        row_index = int(row1)

        column_difference = abs((ord(column2) - 64) - (ord(column1) - 64))
        row_difference = abs(int(row2) - int(row1))

        # Diagonal movement (like bishop)
        if column_difference == row_difference:
            # Up and to the right
            if (row_index < int(row2)) and (column_index < (ord(column2) - 64)):
                while row_index < (int(row2) - 1) and column_index < ((ord(column2) - 64) - 1):
                    row_index += 1
                    column_index += 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement is up to the right is blocked by another piece.")
                        return False
                return True
            # Up and to the left
            elif (row_index < int(row2)) and (column_index > (ord(column2) - 64)):
                while row_index < (int(row2) - 1) and (column_index > (ord(column2) - 64) + 1):
                    row_index += 1
                    column_index -= 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement up to the left is blocked by another piece.")
                        return False
                return True
            # Down and to the left
            elif (row_index > int(row2)) and (column_index > (ord(column2) - 64)):
                while row_index > (int(row2) + 1) and (column_index > (ord(column2) - 64) + 1):
                    row_index -= 1
                    column_index -= 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement down and to the left is blocked by another piece.")
                        return False
                return True
            # Down and to the right
            elif (row_index > int(row2)) and (column_index < (ord(column2) - 64)):
                while row_index > (int(row2) + 1) and (column_index < (ord(column2) - 64) - 1):
                    row_index -= 1
                    column_index += 1
                    if board[chr(column_index + 64)][str(row_index)] is not None:
                        print("Error: The diagonal movement down to the right is blocked by another piece.")
                        return False
                return True
        # If the difference in rows > 0 and the difference in columns == 0, the move is vertical.
        elif row_difference > 0 and column_difference == 0:
            # moving up
            if row_index < int(row2):
                while row_index < (int(row2) - 1):
                    row_index += 1
                    if board[column1][str(row_index)] is not None:
                        print("Error: The vertical movement upward is blocked by another piece.")
                        return False
                return True
            # moving down
            elif int(row1) > int(row2):
                while row_index > (int(row2) + 1):
                    row_index -= 1
                    if board[column1][str(row_index)] is not None:
                        print("Error: The vertical movement downward is blocked by another piece.")
                        return False
                return True

        # If the difference in columns > 0 and the difference in rows == 0, the move is horizontal.
        elif column_difference > 0 and row_difference == 0:
            # Moving to the right
            if (ord(column1) - 64) < (ord(column2) - 64):
                while column_index < ((ord(column2) - 64) + 1):
                    column_index += 1
                    if board[chr(column_index + 64)][row1] is not None:
                        print("Error: The horizontal movement is blocked by another piece.")
                        return False
                return True
            # Moving to the left
            elif (ord(column1) - 64) > (ord(column2) - 64):
                while row_index > (int(row2) + 1):
                    row_index -= 1
                    if board[str(row_index)][row1] is not None:
                        print("Error: The horizontal movement to the left is blocked by another piece.")
                return True
        else:
            return False


class King(Piece):
    """
    Represents a type of piece that can only move one space
    at a time in cardinal directions or diagonally.
    """

    def __init__(self, team, position):
        """
         Initializes a King piece with its team and starting board position.
         """
        super().__init__(team, position)

        self._type = 'King'

    def is_valid_move(self, move_to, board):
        """
        Checks if move is a valid move for a King. Returns true if valid, false if invalid
        """

        column1 = self._column
        row1 = self._row

        column2 = move_to[0]
        row2 = move_to[1]

        valid_rows = [row1, str(int(row1) + 1), str(int(row1) + 1)]
        valid_columns = [column1, chr(ord(column1) + 1), chr(ord(column1) - 1)]

        if row2 in valid_rows and column2 in valid_columns:
            return True
        else:
            return False
