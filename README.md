    This project is a playable implementation of Chess written in Python. A player wins in this variant by capturing all the pieces
    of one type of piece belonging to the opposing player.

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
