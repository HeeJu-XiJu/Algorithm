def solution(dots):
    x_list = []
    y_list = []

    for i in range(3):
        for j in range(i+1, 4):
            x_list.append(abs(dots[i][0] - dots[j][0])) # x좌표 차
            y_list.append(abs(dots[i][1] - dots[j][1])) # y좌표 차
            print(i, j)

    if x_list[0] / x_list[5] == y_list[0] / y_list[5]:
        answer = 1
    elif x_list[1] / x_list[4] == y_list[1] / y_list[4]:
        answer = 1
    elif x_list[2] / x_list[3] == y_list[2] / y_list[3]:
        answer = 1
    else :
        answer = 0
            
    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))        