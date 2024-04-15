class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #{k: [] for k in range(9)}
        cols = collections.defaultdict(set) #{k: [] for k in range(9)}
        squares = collections.defaultdict(set) #{(i, j): [] for i in range(4) for j in range(4)}

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                square = (i//3, j//3)
                if n != '.':
                    if (n in rows[i]
                        or n in cols[j]
                        or n in squares[square]):
                        return False
                    rows[i].add(n)
                    cols[j].add(n)
                    squares[square].add(n)
        return True