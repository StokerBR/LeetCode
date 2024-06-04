class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.search(board, i, j, word):
                        return True

        return False

    def search(self, board, i, j, word):
        word = word[1:]
        if len(word) == 0:
            return True
        tmp = board[i][j]
        board[i][j] = ''
        adjacent = self.getAdjacent(board, i, j)
        for (i1, j1) in adjacent:
            if board[i1][j1] == word[0]:
                if self.search(board, i1, j1, word):
                    return True
        board[i][j] = tmp
        return False

    def getAdjacent(self, board, i, j):
        m = len(board)
        n = len(board[0])
        adjacent = []
        if i-1 >= 0:
            adjacent.append((i-1, j))
        if i+1 < m:
            adjacent.append((i+1, j))
        if j-1 >= 0:
            adjacent.append((i, j-1))
        if j+1 < n:
            adjacent.append((i, j+1))
        return adjacent