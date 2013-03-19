/* Go is a 2 player board game with simple rules. Two players alternate turns
 * placing stones on a grid. If a stone is surrounded on 4 sides by stones of
 * the opponent, it is captured. If a group of stones are surrounded, they are
 * captured.
 * See http://en.wikipedia.org/wiki/Rules_of_Go#Capture for a visual explanation.
 * 
 * Below is an implementation of a Go board. Please write some code in the
 * move() function to check for captures and output something when a capture
 * occurs. The sample moves represent a capture of two black stones.
 */

#include <stdio.h>
#include <string.h>

#define BOARD_SIZE 19

typedef unsigned char board_t[BOARD_SIZE][BOARD_SIZE];

enum {
    EMPTY = 0x1,
    BLACK = 0x2,
    WHITE = 0x4,
};

int move(board_t board, int color, size_t row, size_t col) {
    board[row][col] = color;
    return 0;
}

void print_board(board_t board) {
    for (size_t r = 0; r < BOARD_SIZE; r++) {
        for (size_t c = 0; c < BOARD_SIZE; c++) {
            if (board[r][c] == EMPTY)
                putchar('_');
            else
                printf("%d", board[r][c]);
        }
        putchar('\n');
    }
}

int main() {
    board_t board;
    memset(board, EMPTY, sizeof(unsigned char) * BOARD_SIZE * BOARD_SIZE);
    move(board, BLACK, 4, 4);
    move(board, BLACK, 4, 5);
    move(board, WHITE, 3, 4);
    move(board, WHITE, 3, 5);
    move(board, WHITE, 4, 3);
    move(board, WHITE, 4, 6);
    move(board, WHITE, 5, 4);
    move(board, WHITE, 5, 5);
    print_board(board);
    return 0;
}