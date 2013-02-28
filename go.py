#!/usr/bin/env python

# Go is a 2 player board game with simple rules. Two players alternate turns
# placing stones on a grid. If a stone is surrounded on 4 sides by stones of
# the opponent, it is captured. If a group of stones are surrounded, they are
# captured.
# See http://en.wikipedia.org/wiki/Rules_of_Go#Capture for a visual explanation.

# Below is an implementation of a Go board. Please write some code in the
# move() method to check for captures and output something when a capture
# occurs. The sample moves represent a capture of two black stones.

EMPTY = 0
BLACK = 1
WHITE = 2

class Board(object):
    def __init__(self):
        self.board = [[EMPTY] * 19 for _ in xrange(19)] # 2d 19x19 matrix of 0's

    def __str__(self):
        s = ''
        for row in self.board:
            if s:
                s += '\n'
            for sq in row:
                if sq:
                    s += str(sq)
                else:
                    s += '_'
        return s

    def move(self, color, row, col):
        self.board[row][col] = color

b = Board()
b.move(BLACK, 4, 4)
b.move(BLACK, 4, 5)
b.move(WHITE, 3, 4)
b.move(WHITE, 3, 5)
b.move(WHITE, 4, 3)
b.move(WHITE, 4, 6)
b.move(WHITE, 5, 4)
b.move(WHITE, 5, 5)
print b