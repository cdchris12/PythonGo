#!/usr/bin/env python

# This is the test suite for my go implementation. Simply execute this file, and it'll run
# the entire test suite for you. :-)

from go import *

def runTestSuite():
    results = []
    results.append( singleEnclosure() )
    results.append( doubleEnclosure() )
    results.append( quadEnclosure() )
    results.append( connDoubleQuadEnclosure() )
    
    if False not in results:
        print "-----ALL TESTS PASSED!!-----"
    else:
        print "-----TESTING FAILED!!-----"
    # End if/else block
# End def

def singleEnclosure():
    b = Board()
    print "Testing a single enclosure:"
    
    b.move(BLACK, 4, 4, True)
    b.move(BLACK, 5, 3, True)
    b.move(WHITE, 5, 4, True)
    b.move(BLACK, 5, 5, True)
    b.move(BLACK, 6, 4, True)
    
    try:
        assert b.board[5][4] == EMPTY
    except AssertionError, e:
        print b
        print "FAIL!!!!\n"
    else:
        print b
        print "PASS!!!!\n"
    # End try/except block
# End def

def doubleEnclosure():
    b = Board()
    print "Testing a double enclosure:"
    
    b.move(BLACK, 4, 4, True)
    b.move(BLACK, 4, 5, True)
    b.move(BLACK, 5, 3, True)
    b.move(WHITE, 5, 4, True)
    b.move(WHITE, 5, 5, True)
    b.move(BLACK, 5, 6, True)
    b.move(BLACK, 6, 4, True)
    b.move(BLACK, 6, 5, True)
    
    try:
        assert b.board[5][4] == EMPTY
        assert b.board[5][5] == EMPTY
    except AssertionError, e:
        print b
        print "FAIL!!!!\n"
    else:
        print b
        print "PASS!!!!\n"
    # End try/except block
# End def

def quadEnclosure():
    b = Board()
    print "Testing a quad enclosure:"
    
    b.move(BLACK, 4, 4, True)
    b.move(BLACK, 4, 5, True)
    b.move(BLACK, 5, 3, True)
    b.move(WHITE, 5, 4, True)
    b.move(WHITE, 5, 5, True)
    b.move(BLACK, 5, 6, True)
    b.move(BLACK, 6, 3, True)
    b.move(WHITE, 6, 4, True)
    b.move(WHITE, 6, 5, True)
    b.move(BLACK, 6, 6, True)
    b.move(BLACK, 7, 4, True)
    b.move(BLACK, 7, 5, True)
    
    try:
        assert b.board[5][4] == EMPTY
        assert b.board[5][5] == EMPTY
        assert b.board[6][4] == EMPTY
        assert b.board[6][5] == EMPTY
    except AssertionError, e:
        print b
        print "FAIL!!!!\n"
    else:
        print b
        print "PASS!!!!\n"
    # End try/except block
# End def

def connDoubleQuadEnclosure():
    b = Board()
    print "Testing a connecting double quad enclosure:"
    
    b.move(BLACK, 4, 4, True)
    b.move(BLACK, 4, 5, True)
    b.move(BLACK, 5, 3, True)
    b.move(WHITE, 5, 4, True)
    b.move(WHITE, 5, 5, True)
    b.move(BLACK, 5, 6, True)
    b.move(BLACK, 5, 7, True)
    b.move(BLACK, 6, 3, True)
    b.move(WHITE, 6, 4, True)
    b.move(WHITE, 6, 5, True)
    b.move(WHITE, 6, 6, True)
    b.move(WHITE, 6, 7, True)
    b.move(BLACK, 6, 8, True)
    b.move(BLACK, 7, 4, True)
    b.move(BLACK, 7, 5, True)
    b.move(WHITE, 7, 6, True)
    b.move(WHITE, 7, 7, True)
    b.move(BLACK, 7, 8, True)
    b.move(BLACK, 8, 6, True)
    b.move(BLACK, 8, 7, True)
    
    try:
        assert b.board[5][4] == EMPTY
        assert b.board[5][5] == EMPTY
        assert b.board[6][4] == EMPTY
        assert b.board[6][5] == EMPTY
        assert b.board[6][6] == EMPTY
        assert b.board[6][7] == EMPTY
        assert b.board[7][6] == EMPTY
        assert b.board[7][7] == EMPTY
    except AssertionError, e:
        print b
        print "FAIL!!!!\n"
    else:
        print b
        print "PASS!!!!\n"
    # End try/except block
# End def

if __name__ == "__main__":
    runTestSuite()
# End if