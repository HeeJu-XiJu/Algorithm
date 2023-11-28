def solution(park, routes):
    answer = [0, 0]
    for n in range(len(park)):
        if 'S' in park[n]:
            answer[0] = n
            answer[1] = park[n].find('S')

    for n in routes:
        d, s = n.split()
        if d == 'E':
            if answer[1]+int(s) >= len(park[0]) or 'X' in park[answer[0]][answer[1]:answer[1]+int(s)+1]:
                pass
            else:
                answer[1] += int(s)
        if d == 'W':
            if answer[1]-int(s) < 0 or 'X' in park[answer[0]][answer[1]-int(s):answer[1]]:
                pass
            else:
                answer[1] -= int(s)
        if d == 'S':
            none = 0
            for i in range(0, int(s)+1):
                if park[answer[0]+i][answer[1]] == 'X':
                    none = 1
            if answer[0]+int(s) >= len(park) or none == 1:
                pass
            else:
                answer[0] += int(s)
        if d == 'N':
            none = 0
            for i in range(0, int(s)+1):
                if park[answer[0]-i][answer[1]] == 'X':
                    none = 1
            if answer[0]-int(s) < 0 or none == 1 :
                pass
            else:
                answer[0] -= int(s)

    return answer


# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))



def solution(park, routes):
    h = len(park)
    w = len(park[0])
    x,y = 0,0
    
    nav = {
        'S': [1,0],
        'N':[-1,0],
        'W': [0,-1],
        'E':[0,1]
    }
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1,distance+1):
            step_x += nav[direction][0]
            step_y += nav[direction][1]
            
            if step_x >= h or step_x <= -1 or step_y >= w or step_y <= -1 or park[step_x][step_y] == 'X':
                flag = 1
                break
            
        if(flag == 0):
            x += nav[direction][0] * distance
            y += nav[direction][1] * distance
    
    answer = [x,y]
    return answer