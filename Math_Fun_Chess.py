
class Chessboard(object):
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

    def get_board(self):
        return self.board

    def count_free_place(self):
        count = 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 0:
                    # 0 means it is free for all
                    count = count+1
        return count

    def place_is_free(self, x, y):
        if self.board[y][x] is 0:
            return True
        return False

    def place_queen_on(self, x, y):
        if self.place_is_free(x, y):
            # for simplicity 2 as queen.
            self.board[y][x] = 2
            for i in range(0, self.height):
                # horizontal
                if self.board[y][i] is 0:
                    self.board[y][i] = 1
                for j in range(0, self.width):
                    # vertical
                    if self.board[i][x] is 0:
                        self.board[i][x] = 1
                    if (i+j) == (x+y) and self.board[i][j] is 0:
                        self.board[i][j] = 1

                    #if self.board[(i+i)%self.width][(j+i)%self.width] is 0:
                        self.board[i][j] = 1
                        # TODO continue here: problem is find and mark top left to bottom right diagonal fo x,y

            return self.board
        else:
            print(str(x) + ", " + str(y) + " is invalid")

    def place_queen_on_next_available_place(self):
        # ordered by y and x.
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 0:
                    # 0 means it is free for all
                    self.place_queen_on(i, j)
                    break

    def __str__(self):
        # EQ für toString
        ret = ""
        for i in range(0, self.height):
            ret += str(self.board[i]) + "\n"
        return ret


#def backtrack(board, free_place_count):


def find_peaceful_place_for_k_queen(board):
    # print(board.count_free_place())
    # board.place_queen_on_next_available_place()
    board.place_queen_on(3, 5)
    print(board)


if __name__ == '__main__':
    c = Chessboard()
    find_peaceful_place_for_k_queen(c)
