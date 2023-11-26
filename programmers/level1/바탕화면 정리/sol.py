def solution(wallpaper):
    answer = [0, 0, 0, 0]
    stack = [] # '#'이 있는 행
    stack1 = [] # '#'이 가장 처음에 있는 열
    stack2 = [] # '#'이 가장 마지막에 있는 열
    
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            stack.append(i)
            stack1.append(wallpaper[i].find('#'))
            stack2.append(wallpaper[i].rfind('#'))

    answer[0] = min(stack)
    answer[2] = max(stack) + 1
    answer[1] = min(stack1)
    answer[3] = max(stack2) + 1

    return answer


print(solution([".#...", "..#..", "...#."]))