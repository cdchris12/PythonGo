#!/usr/bin/env python

# Go is a 2 player board game with simple rules. Two players alternate turns
# placing stones on a grid. If a stone is surrounded on 4 sides by stones of
# the opponent, it is captured. If a group of stones are surrounded, they are
# captured.
# See http://en.wikipedia.org/wiki/Rules_of_Go#Capture for a visual explanation.

# Below is an implementation of a Go board. Please write some code in the
# move() method to check for captures and output something when a capture
# occurs. The sample moves represent a capture of two black stones.

from copy import deepcopy
from test import *

EMPTY = 0
BLACK = 1
WHITE = 2
RED = 3

class Board(object):
    def __init__(self):
        self.board = [[EMPTY] * 19 for _ in xrange(19)] # 2d 19x19 matrix of 0's
    # End def

    def __str__(self):
        s = ''
        for row in self.board:
            if s:
                s += '\n'
            # End if
            for sq in row:
                if sq:
                    s += str(sq)
                else:
                    s += '_'
                # End if/else block
            # End for
        # End for
        
        return s
    # End def

    def move(self, color, row, col, test=False):
        self.board[row][col] = color
        if not test: 
            print "Row %s, col %s was set to %s." % (row, col, "white" if color == WHITE else "black")
        # End if
        self.checkNewMove(row, col, color, test)
    # End def
    
    def checkNewMove(self, row, col, color, test=False):
        new_board = deepcopy(self.board) # Make a copy of the board, just so we won't have to do as much cleaning when we are done
        
        other_color = BLACK if color == WHITE else WHITE
        
        for a in [(0,+1),(0,-1),(+1,0),(-1,0)]:
            ret, checked = self.search(row + a[0], col + a[1], other_color, new_board)
            if ret: # If we have an enclosure,
                checked = set(checked)
                for spot in checked:
                    if not test:
                        print "Removing tile at row %s, col %s because it was enclosed!!" % (spot[0], spot[1])
                    self.board[spot[0]][spot[1]] = EMPTY # Remove all the enclosed tiles
                # End for
            # End if
        # End for
        # This for loop of if statements is going to do a rudimentary check for each of the 4
        # directions a move could touch. Then, we're going to do a search for possible
        # enclosures. It is possible for a single piece to enclose three or even four
        # sets of squares, so we should check all four touched squares every time.
        
        del new_board # This isn't specifically required, as Python will automatically garbage
        # collect this object, but no harm in forcing its hand a bit early.. :-)
    # End def
    
    def search(self, row, col, color, new_board):
        other_color = BLACK if color == WHITE else WHITE
        
        checked = []
        for a in [(0,+1),(0,-1),(+1,0),(-1,0),]:
            if new_board[row + a[0]][col + a[1]] == color: # Mark this spot as contiguous
                new_board[row + a[0]][col + a[1]] = RED
                checked.append( (row + a[0], col + a[1]) ) # Keep track of the spots we've marked as part of this collection
                ret, new_checked = self.search(row + a[0], col + a[1], color, new_board) # Use recursion to check cells until we're done
                if ret:
                    for item in new_checked: checked.append(item)
                else:
                    return ( (False, []) )
                # End if/else block
            elif new_board[row + a[0]][col + a[1]] == EMPTY: # This search is fruitless, as we have discovered an empty space
                return ( (False, []) )
            # End else/if block
        # End for
        
        if checked == []: # This coveres the single enclosed tile case
            checked.append( (row,col) )
        # End if
        
        return ( (True, checked) )
    # End def
# End class

def main():
    '''b = Board()
    b.move(BLACK, 4, 4)
    b.move(BLACK, 4, 5)
    b.move(WHITE, 3, 4)
    b.move(WHITE, 3, 5)
    b.move(WHITE, 4, 3)
    b.move(WHITE, 4, 6)
    b.move(WHITE, 5, 4)
    b.move(WHITE, 5, 5)
    print b'''
    
    runTestSuite()
# End def

if __name__ == "__main__":
    main()
# End if
