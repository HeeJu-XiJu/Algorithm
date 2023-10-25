def solution(keyinput, board):
    answer = [0, 0]
    for key in keyinput:
        if key == 'left':
            answer[0] -= 1
        elif key == 'right':
            answer[0] += 1
    
        elif key == 'up':
            answer[1] += 1
        elif key == 'down':
            answer[1] -= 1

        if answer[0] > (board[0] // 2) :
            answer[0] -= 1
        elif answer[0] < -(board[0] // 2) :
            answer[0] += 1
        elif answer[1] > (board[1] // 2) :
            answer[1] -= 1
        elif answer[1] < -(board[1] // 2) :
            answer[1] += 1

    return answer

print(solution(["left", "right", "up", "right", "right"], [11, 11]))