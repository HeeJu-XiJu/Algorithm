def solution (keyinput, board):
    board (4, 4)
    now = [4, 0]

    for key in keyinput:
        if -(board[0]//2) < now[0] < board[0]//2:
            if key == 'left':
                now = [now[0]-1, now[1]]
            if key == 'right':
                now = [now[0]+1, now[1]] 
        else: 
            now = now

        if -(board[1]//2) < now[1] < board[1]//2:
            if key == 'up':
                now = [now[0], now[1]+1]
            if key == 'down':
                now = [now[0], now[1]-1]
        else:
            now = now

    return now

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))