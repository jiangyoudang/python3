
def find(board, word, pos, visited):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    found = False
    if not word:
        return True
    for direction in directions:
        x, y = pos
        x_di, y_di = direction
        x += x_di
        y += y_di
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if (x, y) not in visited and board[x][y] == word[0]:
                visited.add((x,y))
                found = find(board, word[1:], (x,y), visited) or found
                if found:
                    return True
                visited.remove((x,y))

    return found

def exist(board, word):
    m = len(board)
    n = len(board[0])
    if not board or n==0:
        return False
    if not word:
        return False
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if find(board, word[1:], (i,j), {(i,j)}):
                    return True
    return False



board = ['abce','sfcs', 'adee']
word = 'abcced'

print(exist(board, word))