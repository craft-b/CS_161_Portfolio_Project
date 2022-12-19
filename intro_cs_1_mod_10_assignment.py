# Bobby Craft
# Date: 4-3-22
# Description: Intro to Comp Sci I: Module 10 Project
#
#  Write a class named FBoard for playing a game, where player x
# is trying to get her piece to corner square (7,7) and player o
# is trying to make it so player x doesn't have any legal moves.
# It should have the following private data members:

# An 8x8 list of lists for tracking what's on each square of the
# board. A data member for tracking the game state, that holds one
# of the following string values: "X_WON", "O_WON", or "UNFINISHED".
# Data members to keep track of where the x piece is.

# **The data members should all be private.**
# * An init method (constructor) that initializes the list of lists
# to represent an empty 8x8 board (you can use whatever character
# you want to represent empty).  It should put four o pieces at the
# following (row, column) coordinates: (5,7), (6,6), (7,5), and (7,7).
# It should put an x piece at (0,0).  It should also initialize the
# other data members.

# * A method called get_game_state, that returns the current value of
# game_state.

# * A method called move_x that takes as parameters the row and column
# of the square to move to.  If the desired move is not allowed, or if
# the game has already been won, it should just return False.  Otherwise
# it should make the move and return True.  A piece belonging to x can
# move 1 square diagonally in any direction.  A piece is not allowed to
# move off the board or to an occupied square.  If x's move gets her piece
# to square (7,7), game_state should be set to "X_WON".

# * A method called move_o that takes as parameters the row and column to move
# from, and the row and column to move to.  If the first pair of coordinates
# doesn't hold o's piece, or if the desired move is not allowed, or if the game
# has already been won, it should just return False.  Othewise it should make
# the move and return True.  A piece belonging to o can move 1 square diagonally,
# **but the row and column cannot both increase**, so any o piece has at most
# three available moves.  For example, if player o has a piece at (5, 1), it could
# move to (4, 0), (4, 2), or (6,0), but not to (6, 2).  It is not allowed to move
# off the board or to an occupied square.  If o's move leaves no legal move for x,
# game_state should be set to "O_WON".

# You do not need to track whose turn it is.  Either move method can be called multiple
# times in a row.

# It doesn't matter which index of the list of lists you consider the row and which you
# consider the column as long as you're consistent.

# Feel free to add helper functions if you want.  You may also find it useful to add a
# print function to help with debugging.

# Here's a very simple example of how the class could be used:
# ```
#   fb = FBoard();
#   fb.move_x(1,1);
#   fb.move_x(2,0);
#   fb.move_o(6,6,5,5);
#   print(fb.get_game_state());
# ```

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


fb = FBoard()
fb.move_x(1, 1)
#fb.move_x(2,0)
fb.move_o(6,6,5,5)
#fb.print_board()
fb.move_o(5,5,6,4)
#fb.print_board()
fb.move_x(2,2)
#fb.print_board()
fb.move_x(3,3)
fb.move_o(7,7,6,6)
fb.move_o(6,6,5,5)
fb.move_o(5,5,4,4)
# fb.move_o(4,4,3,3)
# fb.move_o(3,3,2,2)
# fb.move_o(2,2,1,1)
fb.move_o(4,4,3,5)
#fb.print_board()
fb.move_x(4,4)
fb.move_x(5,5)
fb.move_x(6,6)
fb.move_x(7,7)
# fb.move_x(1, 1)

print(fb.get_game_state())
fb.print_board()
