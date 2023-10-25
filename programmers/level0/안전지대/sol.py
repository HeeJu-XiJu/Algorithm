def solution(board):
    bomb = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bomb.append([i, j])

    rev_board = board
    for i in bomb:
        x, y = i
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= x + k < len(board) and 0 <= y + l < len(board):
                    rev_board[x+k][y+l] = 1
    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if rev_board[i][j] == 0:
                answer += 1
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))