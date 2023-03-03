# Bobby Craft
# Date: 4-3-22
# Description: Intro to Comp Sci I: Module 10 Project


class FBoard:
    """
    Set-up new gameboard
    """
    def __init__(self):
        self._board = [["*" for j in range(8)] for i in range(8)]
        self._game_sate = "UNFINISHED" # "X_WON, O_WON, or UNFINISHED"
        self._board[5][7] = "o"
        self._board[6][6] = "o"
        self._board[7][5] = "o"
        self._board[7][7] = "o"
        self._board[0][0] = "x"
        self._x_row = 0 # tracks x's x-coord
        self._x_col = 0 # tracks x's y-coord


    def get_game_state(self):
        return self._game_sate
    

    def is_move_in_range(self, row, col):
        """
        Return False if move not on board
        """
        return row in range(8) and col in range(8)
       
        
    def is_move_legal(self, to_row, to_col):
        """
        Return False if move not allowed or 
        True if valid.
        """
        if self.get_game_state() != "UNFINISHED":
            return False

        if not self.is_move_in_range(to_row, to_col):
            return False

        # If destination is not empty and game is not won
        if self._board[to_row][to_col] != "*" and not self.check_if_won():
            print("Move is invalid. Please try again.")
            return False

        return True


    def valid_x_move(self, to_row, to_col):
        """
        Check if x can move diagonally by 1 square in any direction.
        Returns True if the move is valid.
        """   
        diagonal_moves = [(self._x_row + 1, self._x_col - 1), 
                      (self._x_row + 1, self._x_col + 1), 
                      (self._x_row - 1, self._x_col - 1), 
                      (self._x_row - 1, self._x_col + 1)]
       
        return (to_row, to_col) in diagonal_moves


    def move_x(self, to_row, to_col):
        """
        Moves x diagonally by one square if the given coordinates 
        are legal.
        """
        if self.is_move_legal(to_row, to_col) and self.valid_x_move(to_row, to_col):
            # Move x
            self._board[self._x_row][self._x_col] = '*'
            self._board[to_row][to_col] = 'x'
            
            # Update x position
            self._x_row, self._x_col = to_row, to_col
            
            self.check_if_won()  # win if x coord is (7,7)
            
            return True
         return False


    def valid_o_move(self,to_row, to_col, fr_row, fr_col):
        """
        Checks if o move is allowed. Returns True if valid.
        """    
        # Starting coordinate can only contain o
        if self._board[fr_row][fr_col] != 'o':
            return False
        
        # Can only move 1 square diagonally.  (to_row, 
        # to_col) can't both increase together 
        elif (to_row, to_col) == (fr_row-1, fr_col+1) or (
            to_row, to_col) == (fr_row-1, fr_col-1) or (
            to_row, to_col) == (fr_row+1, fr_col-1):
            return True
                

    def move_o(self, fr_row, fr_col, to_row, to_col):
        """
        Moves 'o' from given origin to destination coordinates 
        if move is legal.
        """
        if self.is_move_legal(to_row, to_col) and \
                self.valid_o_move(to_row, to_col, fr_row, fr_col):
            # Move 'o'
            self._board[fr_row][fr_col] = '*'
            self._board[to_row][to_col] = 'o'
            return True
        return False
    

    def check_surrounding_squares(self, r, c):
        """
        Returns a list of out-of-bounds or occupied diagonal 
        moves from the given starting row and column.
        """
        offsets = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        bad_moves = []
        for dr, dc in offsets:
            row, col = r + dr, c + dc
            if not self.is_move_in_range(row, col) or self._board[row][col] != '*':
                bad_moves.append((row, col))
        return bad_moves


    def check_if_won(self):
        """
        Checks if the game has been won.
        """
        bad_moves = self.check_surrounding_squares(self._x_row, self._x_col)
        if self._board[7][7] == "x":
            self._game_sate = "X_WON"
            return True
        elif len(bad_moves) == 4:
            self._game_sate = "O_WON"
            return True
        else:
            bad_moves.clear()
            return False
  
        
    def print_board(self):
        "Visualization of gameboard"
        print(*self._board, sep='\n')


