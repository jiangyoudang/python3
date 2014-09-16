class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return

        queue = set()
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            board[row] = (list(board[row]))

        for j in range(cols):
            if board[0][j] == 'O':
                queue.add((0,j))
            if board[rows-1][j] == 'O':
                queue.add((rows-1,j))
        for i in range(1,rows-1):
            if board[i][0] == 'O':
                queue.add((i,0))
            if board[i][cols-1] == 'O':
                queue.add((i,cols-1))

        while queue:
            curr = queue.pop()
            x, y = curr
            board[x][y] = 'Q'
            if x+1<rows-1 and board[x+1][y]=='O':
                queue.add((x+1,y))
            if x-1>0 and board[x-1][y] == 'O':
                queue.add((x-1,y))
            if y+1<cols-1 and board[x][y+1] == 'O':
                queue.add((x,y+1))
            if y-1>0 and board[x][y-1] == 'O':
                queue.add((x,y-1))


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'Q':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

        for row in range(rows):
            board[row] = ''.join(board[row])



test = Solution()
board = ["XXX","XOX","XXX"]
res = test.solve(board)
print(board)