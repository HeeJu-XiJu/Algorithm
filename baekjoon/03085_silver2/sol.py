import sys
sys.stdin = open('input.txt')

N = int(input())

board = [list(input()) for _ in range(N)]


def check(list):
    maxcount = 1
    for i in range(N):
    # 가로
        count = 1
        for j in range(N-1):
            if list[i][j] == list[i][j+1]:
                count += 1
            else:
                count = 1
            maxcount = max(maxcount, count)
    
    # 세로
        count = 1
        for j in range(N-1):
            if list[j][i] == list[j+1][i]:
                count += 1
            else:
                count = 1
            maxcount = max(count, maxcount)
    return maxcount

maxcount = 1
for i in range(N):
    for j in range(N-1):
# 가로 swap
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        maxcount = max(maxcount, check(board))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
# 세로 swap
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        maxcount = max(maxcount, check(board))
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(maxcount)