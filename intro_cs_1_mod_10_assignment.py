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
    

    def is_move_in_range(self,r,c):
        """
        Return False if move not on board
        """
        if r not in range(0,8) or c not in range(0,8):
            return False
        return True
       
        
    def if_move_legal(self, to_row, to_col):
        """
        Return False if move not allowed or 
        True if valid.
        """     
        # If Game is over.
        if self.get_game_state() != "UNFINISHED":
            return False
        
        # If move is out-of-range.
        if self.is_move_in_range(to_row, to_col) == False:
            return False

        # If destination is not empty
        if self._board[to_row][to_col] != "*":
            # Check if game's over 
            if self.check_if_won() != True:
                print("Move is invalid. Please try again.")
                return  # Try another square
            return False   
        return True


    def valid_x_move(self, to_row, to_col):
        """
        x only moves diagonally.  Checks move 
        validity. Returns True if diagonal.
        """    
        # Only move 1 square diagonally any direction
        if (to_row, to_col) == (self._x_row+1, self._x_col-1) or (
            to_row, to_col) == (self._x_row+1, self._x_col+1) or (
            to_row, to_col) == (self._x_row-1, self._x_col-1) or (
            to_row, to_col) == (self._x_row-1, self._x_col+1):
            return True   
        return False # move not allowed


    def move_x(self, to_row, to_col):
        """
        Moves x one square diagonally, 
        if input(row,col) is legal. 
        """
        if self.if_move_legal(to_row, to_col) == True: 
            if self.valid_x_move(to_row, to_col) == True:
                # Move x
                self._board[self._x_row][self._x_col] = '*'
                self._board[to_row][to_col] = 'x'
                # Update x position
                self._x_row = to_row
                self._x_col = to_col
                self.check_if_won() # win if x coord is (7,7)
                return True


    def valid_o_move(self,to_row, to_col, fr_row, fr_col):
        """
        Checks if o move is allowed.  
        Returns True if valid.
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
        Takes origin and destination coordinates.
        Moves o if valid. 
        """
        if self.if_move_legal(to_row, to_col) == True: 
            if self.valid_o_move(to_row, to_col, fr_row, fr_col) == True:
                # Move o
                self._board[fr_row][fr_col] = '*'
                self._board[to_row][to_col] = 'o'
            return True
    

    def check_surrounding_squares(self, r, c): 
        """
        Takes starting row, col. Checks sourrounding
        diagonal moves. Of these, returns list of 
        out-of-bounds or occupied coordinates. 
        """
        bad_moves = []

        if not self.is_move_in_range(r+1, c+1) or  \
            self._board[r+1][c+1] != '*':
            bad_moves.append((r+1,c+1))
        
        if not self.is_move_in_range(r-1, c-1) or \
            self._board[r-1][c-1] != '*':
            bad_moves.append((r-1,c-1))
        
        if not self.is_move_in_range(r-1, c+1) or \
            self._board[r-1][c+1] != '*':
            bad_moves.append((r-1,c+1))
        
        if not self.is_move_in_range(r+1, c-1) or \
            self._board[r+1][c-1] != '*':
            bad_moves.append((r+1,c-1))     
        return bad_moves


    def check_if_won(self):
        """
        Check move for the win.
        """
        r = self._x_row  # Starting row
        c = self._x_col  # Staring col 
        bad_moves = self.check_surrounding_squares(r,c)

        if self._board[7][7] == "x":
            self._game_sate = "X_WON"   
            return True
        elif len(bad_moves) == 4:
            self._game_sate = "O_WON"
            return True
        else:
            bad_moves.clear()   # "UNFINISHED"
  
        
    def print_board(self):
        "Visualization of gameboard"
        for i in self._board:
            print(i)


