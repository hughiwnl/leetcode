class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # remember defaultdict of sets and lists
        # we use a set here because it's O(1) time to check for an element
        # list is o(n) since it's linear
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
'''
if our board was:
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

rows would map out into:
{
  0: {"5","3","7"},
  1: {"6","1","9","5"},
  2: {"9","8","6"},
  3: {"8","6","3"},
  4: {"4","8","3","1"},
  5: {"7","2","6"},
  6: {"6","2","8"},
  7: {"4","1","9","5"},
  8: {"8","7","9"}
}
cols would map out into
{
  0: {"5","6","8","4","7"},
  1: {"3","9","6"},
  2: {"8"},
  3: {"1","8","4"},
  4: {"7","9","6","2","1","8"},
  5: {"5","3","9"},
  6: {"2"},
  7: {"6","8","7"},
  8: {"3","1","6","5","9"}
}
squares would map out into
{
  (0,0): {"5","3","6","9","8"},
  (0,1): {"7","1","9","5"},
  (0,2): {"6"},
  (1,0): {"8","4","7"},
  (1,1): {"6","8","3","2"},
  (1,2): {"3","1","6"},
  (2,0): {"6"},
  (2,1): {"4","1","9","8"},
  (2,2): {"2","8","5","7","9"}
}

'''
