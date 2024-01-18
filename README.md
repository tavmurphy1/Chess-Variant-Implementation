# Overview
Welcome to the Chess Variant - Piece Capture, a playable implementation of Chess written in Python. In this unique variant, the objective is to secure victory by capturing all the pieces of one type belonging to the opposing player.

# Features
Data Members
game_state: Represents the current state of the game.
current_turn: Indicates whose player's turn it is.
board: A list of dictionaries representing 8x8 squares and their Piece occupants.
white_pieces: A dictionary containing a running count of white pieces remaining, categorized by type.
black_pieces: Similar to white_pieces but for black pieces.
# Methods
make_move: Moves a piece from one square to another if and only if the movement is valid. Returns 'True' if the move is valid and successfully completed, and 'False' if the move is invalid. Communicates with the Piece class and its subclasses to determine the validity of moves.
get_game_state: Returns the current game state, which can be 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'.
get_current_turn: Returns the player whose turn it currently is.
get_board: Returns a representation of the current board state.
get_white_pieces_remaining: Returns the dictionary containing counts of white pieces remaining.
get_black_pieces_remaining: Returns the dictionary containing counts of black pieces remaining.
Usage
python
Copy code


# Example usage of the Chess Variant - Piece Capture
chess_game = ChessVariant()
chess_game.make_move('e2', 'e4')
game_state = chess_game.get_game_state()
current_turn = chess_game.get_current_turn()
board_state = chess_game.get_board()
white_pieces_remaining = chess_game.get_white_pieces_remaining()
black_pieces_remaining = chess_game.get_black_pieces_remaining()
