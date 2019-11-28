import random
class Chessboard(object):
    def __init__(self, width = 8, height = 8, para_board=None):
        self.width = width
        self.height = height

        self.board = []

        if para_board is not None:
            if type(para_board) is Chessboard:
                self.board = para_board.board
            if type(para_board) is list:
                self.board = para_board
        else:
            for i in range(0, self.height):
                row = []
                for j in range(0, self.width):
                    row.append(0)
                self.board.append(row)

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

    def list_of_free_cells(self):
        result = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 0:
                    result.append([j,i])
        return result

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
                    elif (x+y) == 0 and (i-j) == 0 and self.board[i][j] is 0:
                        self.board[i][j] = 1

                    if x > y:
                        if x-y == j-i and self.board[i][j] is 0:
                            self.board[i][j] = 1
                    elif y > x:
                        if y - x == i - j and self.board[i][j] is 0:
                            self.board[i][j] = 1

            return True
        else:
#            print(str(x) + ", " + str(y) + " is invalid")
            return False

    def place_queen_on_next_available_place(self):
        # ordered by y and x.
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 0:
                    return self.place_queen_on(j, i)

    def place_queen_on_next_available_random_place(self):
        list_free_places = []
        # ordered by y and x.
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 0:
                    list_free_places.append([j, i])
        if list_free_places.__len__() != 0:
            # print(list_free_places)   # debug
            import random
            random_num = random.randrange(0, list_free_places.__len__())
            random_pick = list_free_places[random_num]
            return self.place_queen_on(random_pick[0], random_pick[1])
        else:
            return self.board

    def count_cell(self, target):
        count = 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is target:
                    count = count+1
        return count

    def clean_invalid_marks(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] is 1:
                    self.board[i][j] = 0

    def validate_queen_collision(self, list_of_queens):
        bool_validation = True
        for i in list_of_queens:
            bool_validation = self.place_queen_on(i[1], i[0])
            if bool_validation is False:
                return bool_validation
        return bool_validation

    def __str__(self):
        # EQ für toString
        ret = ""
        for i in range(0, self.height):
            ret += str(self.board[i]) + "\n"
        return ret


def find_k_queens_greedy(para_board, para_count_free_place):
    if para_count_free_place == 0:
        # if no free cell is available, it is considered done.
        queen_count = para_board.count_cell(2)  # 2 is just temporary num for Queen
        print("Find k queens greedy algorithm "+"placed Queen count = " + str(queen_count))
        print(para_board)
        return para_board
    else:
        # next free place is found by two dimensional array iteration, it makes this method deterministic
        board = Chessboard(para_board.place_queen_on_next_available_place())
        find_k_queens_greedy(board, board.count_free_place())


def find_k_queens_random(para_board, para_count_free_place):
    if para_count_free_place == 0:
        queen_count = para_board.count_cell(2)  # 2 is just temporary num for Queen
        print("Find k queens random pick "+"placed Queen count = " + str(queen_count))
        print(para_board)
        return para_board
    else:
        board = Chessboard(para_board.place_queen_on_next_available_random_place())
        find_k_queens_random(board, board.count_free_place())


def find_k_queens_similar_branch_and_bound(para_board, para_count_free_place):
    if para_count_free_place == 0:
        # if no free cell is available, it is considered done.
        # if you want to consider recursion depth to be termination requirement, import sys and sys.getrecursionlimit()
        queen_count = para_board.count_cell(2)  # 2 is just temporary num for Queen
        print("Backtrack_ordered "+"placed Queen count = " + str(queen_count))
        print(para_board)
        return para_board
    else:
        # list of free cells are gathered.
        list_free_cells = para_board.list_of_free_cells()
        if list_free_cells.__len__() > 1:
            first_candidate = list_free_cells[0]
            second_candidate = list_free_cells[1]

            import copy  # leave it for better understanding codes below (python compiler will fix this automatically)
            # deepcopy because implicit shallow copies are configured to save memory,
            # therefor it copies references instead of (needed) instances
            board_0 = copy.deepcopy(para_board)
            board_1 = copy.deepcopy(para_board)

            board_0.place_queen_on(first_candidate[0], first_candidate[1])
            board_1.place_queen_on(second_candidate[0], second_candidate[1])

            find_k_queens_similar_branch_and_bound(board_0, board_0.count_free_place())
            find_k_queens_similar_branch_and_bound(board_1, board_1.count_free_place())

        else:
            board = Chessboard(para_board.place_queen_on_next_available_place())
            find_k_queens_similar_branch_and_bound(board, board.count_free_place())


def find_k_queens_backtrack(para_candidates, depth):
    import copy
    # candidates = remained free cells on chess board, candidates are empty at start.
    # depth = recursion depth or let's say depth of the back track tree. It starts with root depth of 0
    #         In find k queens puzzle, the depth limit is width or height of rectangle chessboard
    depth_limit = 4  # if depth_limit = 8, then the board is size of 8 x 8.

    if depth is depth_limit:
        board = Chessboard(depth_limit, depth_limit)

        if board.validate_queen_collision(para_candidates):
            print("")
            print("---TRUE---")
            print(board)
            return True
        print("---FALSE---"+str(para_candidates))
        return False

        # process solution
    else:
        # board = Chessboard(depth_limit, depth_limit)
        for i in range(0, depth_limit):
            next_candidates = copy.deepcopy(para_candidates)
            next_candidates.append([depth, i])
            find_k_queens_backtrack(next_candidates, depth + 1)



if __name__ == '__main__':

    # c0 = Chessboard()
    # greedy_find_k_queens(c0, c0.count_free_place())

    # c1 = Chessboard()
    # find_k_queens_similar_branch_and_bound(c1, c1.count_free_place())

    #c2 = Chessboard()
    #find_k_queens_random(c2, c2.count_free_place())
    find_k_queens_backtrack([], 0)
